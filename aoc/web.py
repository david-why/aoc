from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from enum import IntEnum
import os

import requests
from bs4 import BeautifulSoup

__all__ = [
    'SESSION_FILE',
    'set_session',
    'get_session',
    'get_input_data',
    'submit_answer',
    'SubmitResultEnum',
    'SubmitResult',
]

SESSION_FILE = os.path.join(os.path.expanduser('~'), '.aoc_session')


def set_session(cookie: str):
    with open(SESSION_FILE, 'w') as f:
        f.write(cookie)


def get_session():
    if not os.path.exists(SESSION_FILE):
        raise RuntimeError('You are not logged in. Please use `aoc auth` to login.')
    with open(SESSION_FILE) as f:
        return f.read().strip()


def get_input_data(year: int, day: int):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    response = requests.get(url, cookies={'session': get_session()})
    response.raise_for_status()
    return response.text


class SubmitResultEnum(IntEnum):
    correct = 1
    too_high = 2
    too_low = 3
    incorrect = 4
    unknown = 5
    wait = 6


@dataclass
class SubmitResult:
    result: SubmitResultEnum
    text: str
    try_after: datetime


# level is 1 or 2
def submit_answer(year: int, day: int, level: int, answer) -> SubmitResult:
    url = f'https://adventofcode.com/{year}/day/{day}/answer'
    response = requests.post(
        url,
        cookies={'session': get_session()},
        data={'level': level, 'answer': str(answer)},
    )
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.select_one('article').text.replace('\n', ' ').replace('  ', ' ')  # type: ignore
    response_time = datetime.strptime(
        response.headers['Date'], '%a, %d %b %Y %H:%M:%S GMT'
    ).replace(tzinfo=timezone.utc)
    enum = parse_result(result)
    if enum == SubmitResultEnum.wait:
        time_str = result.partition('trying again. You have ')[2].partition(
            ' left to wait.'
        )[0]
        if ' ' in time_str:  # 2m 23s
            minutes, seconds = time_str.split()
            try_after = response_time + timedelta(
                minutes=int(minutes[:-1]), seconds=int(seconds[:-1])
            )
        elif 's' in time_str:  # 23s
            try_after = response_time + timedelta(seconds=int(time_str[:-1]))
        else:  # 2m
            try_after = response_time + timedelta(minutes=int(time_str[:-1]))
    elif 'please wait 5 minutes' in result:
        try_after = response_time + timedelta(minutes=5)
    elif 'Please wait one minute' in result:
        try_after = response_time + timedelta(minutes=1)
    else:
        try_after = response_time
    return SubmitResult(enum, result, try_after)


def parse_result(text: str) -> SubmitResultEnum:
    if 'the right answer!' in text:
        return SubmitResultEnum.correct
    if 'your answer is too high' in text:
        return SubmitResultEnum.too_high
    if 'your answer is too low' in text:
        return SubmitResultEnum.too_low
    if 'not the right answer' in text:
        return SubmitResultEnum.incorrect
    if 'you have to wait after submitting' in text:
        return SubmitResultEnum.wait
    return SubmitResultEnum.unknown
