# Advent of Code solution for 2024/3.
# why are there 2 tests why why why why why why why why why why why why why
import re
from aoc.lib import *


tm=re.compile(r"mul\(([0-9]+?),([0-9]+?)\)")
tm2=re.compile(r"do\(\)|don't\(\)|mul\(([0-9]+?),([0-9]+?)\)")

T1 = int
T2 = int

testans1: T1 = None  # type: ignore
testans2: T2 = None  # type: ignore
ans1: T1 = None  # type: ignore
ans2: T2 = None  # type: ignore


def solve1(data: str) -> T1:
    # n,d=spl(data)
    ans=0
    for m in tm.finditer(data):
        a,b=map(int,m.groups())
        ans += a*b
    return ans


def solve2(data: str) -> T2:
    n,d=spl(data)
    # n,d=spl(data)
    ans=0
    f=1
    for m in tm2.finditer(data):
        if m.group(1):
            a,b=map(int,m.groups())
            ans += a*b*f
        # dont
        elif data[m.start():m.end()]=="don't()":
            f=0
        # do
        else:f=1
    return ans


if __name__ == '__main__':
    run()
