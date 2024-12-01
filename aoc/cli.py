import os
import time
import json

import click

from aoc.web import get_input_data, set_session

_now = time.localtime()
CURRENT_YEAR = _now.tm_year
# FIXME day for pacific time
CURRENT_DAY = _now.tm_mday if _now.tm_mon == 12 and _now.tm_mday <= 25 else None
del _now

ctx = {'year': CURRENT_YEAR}


def format_dur(seconds: float) -> str:
    if seconds < 60:
        return f'{seconds:.1f}s'
    seconds = int(seconds)
    if seconds < 3600:
        return f'{seconds // 60}m {seconds % 60}s'
    return f'{seconds // 3600}h {(seconds % 3600) // 60}m'


@click.group()
@click.option('--year', default=CURRENT_YEAR, help='The year of the Advent of Code')
def cli(year: int):
    ctx['year'] = year


@cli.command()
@click.argument('cookie')
def auth(cookie: str):
    set_session(cookie)


@cli.command()
@click.option('--day', default=CURRENT_DAY, help='The day of the Advent of Code')
def download(day: int):
    year: int = ctx['year']
    data = get_input_data(year, day)
    os.makedirs(f'{year}', exist_ok=True)
    with open(f'{year}/day{day}.txt', 'w') as f:
        f.write(data)


@cli.command()
@click.option(
    '--day', type=int, default=CURRENT_DAY, help='The day of the Advent of Code'
)
@click.option('--download/--no-download', default=True, help='Download the input data')
@click.option(
    '--code/--no-code', default=False, help='Whether to open VS Code with the files'
)
@click.option('--yes', '-y', is_flag=True, help='Override without asking')
def init(day: int | None, download: bool, code: bool, yes: bool):
    if day is None:
        click.echo(
            'Today is not an Advent of Code day, and no --day is specified. Exiting!',
            err=True,
        )
        return 1
    year: int = ctx['year']
    os.makedirs(f'{year}', exist_ok=True)
    if (
        not os.path.exists(f'{year}/day{day}.py')
        or yes
        or click.confirm('The Python file already exists. Override? ')
    ):
        with open(f'{year}/day{day}.py', 'w') as f:
            f.write(TEMPLATE.format(year=year, day=day))
    if not os.path.exists(f'{year}/day{day}.test'):
        with open(f'{year}/day{day}.test', 'w') as f:
            pass
    if not os.path.exists(f'{year}/day{day}.json'):
        with open(f'{year}/day{day}.json', 'w') as f:
            json.dump({'year': year, 'day': day, 'level': 1}, f)
    if code:
        files = f'{year}/day{day}.test {year}/day{day}.py'
        os.system(f'code {files}')
    if download:
        if (
            not os.path.exists(f'{year}/day{day}.in')
            or yes
            or click.confirm('The input file already exists. Override? ')
        ):
            wait_until = (
                time.mktime(
                    time.strptime(f'{year}-12-{day} 00:00:00', '%Y-%m-%d %H:%M:%S')
                )
                - time.timezone
                + 5 * 3600
            )
            if time.time() < wait_until:
                wait_for = wait_until - time.time()
                click.echo(f"Waiting {format_dur(wait_for)} to download the input data")
                time.sleep(wait_for)
            click.echo('Downloading input data')
            data = get_input_data(year, day)
            with open(f'{year}/day{day}.in', 'w') as f:
                f.write(data)


TEMPLATE = '''\
# Advent of Code solution for {year}/{day}.
from aoc.lib import *

T1 = int
T2 = int

testans1: T1 = None  # type: ignore
testans2: T2 = None  # type: ignore
ans1: T1 = None  # type: ignore
ans2: T2 = None  # type: ignore


def solve1(data: str) -> T1:
    n,d=spl(data)
    
    return 


def solve2(data: str) -> T2:
    n,d=spl(data)
    
    return 


if __name__ == '__main__':
    run()
'''

if __name__ == '__main__':
    cli()
