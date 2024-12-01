# Advent of Code solution for 2024/1.
from aoc.lib import *

T1 = int
T2 = int

testans1: T1 = None  # type: ignore
testans2: T2 = None  # type: ignore
ans1: T1 = None  # type: ignore
ans2: T2 = None  # type: ignore


def solve1(data: str) -> T1:
    n,d=spl(data)
    x=[x.split() for x in d]
    a1=sorted(map(int, (x[0] for x in x)))
    a2=sorted(map(int, (x[1] for x in x)))
    ans = 0
    for a,b in zip(a1,a2):
        ans+=abs(a-b)
    return ans


def solve2(data: str) -> T2:
    n,d=spl(data)
    x=[x.split() for x in d]
    a1=sorted(map(int, (x[0] for x in x)))
    a2=sorted(map(int, (x[1] for x in x)))
    ans=0
    for x in a1:
        ans+=a2.count(x)*x
    return ans


if __name__ == '__main__':
    run(submit=1, year=2024, day=1)
