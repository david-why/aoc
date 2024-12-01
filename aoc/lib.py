import inspect
import json
import os
import time

import click

from aoc.web import SubmitResultEnum, get_input_data, submit_answer


def run(**kwargs) -> None:
    frame = inspect.stack()[1]
    filename = frame.filename
    file_base = os.path.join(
        os.path.dirname(os.path.abspath(filename)),
        os.path.splitext(filename)[0],
    )

    state_file = file_base + '.json'
    with open(state_file) as f:
        state = json.load(f)
    kwargs.update(state)
    year = kwargs['year']
    day = kwargs['day']
    level = kwargs.get('level', 0)

    test_file = file_base + '.test'
    with open(test_file) as f:
        test_data = f.read()
    input_file = file_base + '.in'
    if os.path.exists(input_file):
        with open(input_file) as f:
            input_data = f.read()
    else:
        click.echo('Downloading input data')
        input_data = get_input_data(year=year, day=day)
        with open(input_file, 'w') as f:
            f.write(input_data)
    try_file = file_base + '.try'
    if os.path.exists(try_file):
        with open(try_file) as f:
            wait_until = float(f.read())
    else:
        wait_until = 0
    glob = frame.frame.f_globals

    t_start = time.time()

    if level == 0:
        click.echo(f'--- Day {day} ---')
        click.echo('Part 1:')
        ans1 = glob['solve1'](input_data)
        click.echo(f'Answer: {ans1}')
        click.echo('Part 2:')
        ans2 = glob['solve2'](input_data)
        click.echo(f'Answer: {ans2}')
    else:
        click.echo(f'--- Day {day} ---')
        click.echo(f'Testing Part {level}:')
        for prev in range(1, level):
            if kwargs.get(f'ans{prev}') is not None:
                glob[f'ans{prev}'] = kwargs[f'ans{prev}']
            if kwargs.get(f'testans{prev}') is not None:
                glob[f'testans{prev}'] = kwargs[f'testans{prev}']
        ans = glob[f'solve{level}'](test_data)
        click.echo(f'{ans}')
        success = click.confirm(
            'Correct? ',
            default=f'testans{level}' not in kwargs or ans == kwargs[f'testans{level}'],
        )
        if success:
            kwargs[f'testans{level}'] = ans
            with open(state_file, 'w') as f:
                json.dump(kwargs, f)
            click.echo(f'Running Part {level}:')
            ans = glob[f'solve{level}'](input_data)
            click.echo(f'{ans}')
            if time.time() < wait_until:
                wait_for = wait_until - time.time()
                click.echo(f'Waiting for submission cooldown ({wait_for:.1f}s)')
                time.sleep(wait_until - time.time())
            click.echo('Submitting answer')
            result = submit_answer(year, day, level, ans)
            click.echo(f'Result: {result.result.name} - {result.text}')
            if result.result != SubmitResultEnum.correct:
                with open(try_file, 'w') as f:
                    f.write(str(result.try_after.timestamp()))
            else:
                kwargs['ans1'] = ans
                kwargs['level'] = level = 2 if level == 1 else 0
            with open(state_file, 'w') as f:
                json.dump(kwargs, f)

    click.echo('Time: {:.3f}s'.format(time.time() - t_start))


def spl(data: str):
    lines = data.strip().splitlines()
    return len(lines), lines
