# Advent of Code solution for 2024/2.
from aoc.lib import *

T1 = int
T2 = int

testans1: T1 = None  # type: ignore
testans2: T2 = None  # type: ignore
ans1: T1 = None  # type: ignore
ans2: T2 = None  # type: ignore


def solve1(data: str) -> T1:
    n,d=spl(data)
    ans=0
    for l in d:
        n=list(map(int,l.split()))
        cur=n[0]
        if not (all(n[i+1]<n[i] for i in range(len(n)-1)) or all(n[i+1]>n[i] for i in range(len(n)-1))):
            continue
        for x in n[1:]:
            if abs(cur-x)<1 or abs(cur-x) >3:
                ans-=1
                break
            cur=x
        ans+=1
    return ans


def solve2(data: str) -> T2:
    n,d=spl(data)
    ans=0
    for l in d:
        n=list(map(int,l.split()))
        cur=n[0]
        flag=True
        if not (all(n[i+1]<n[i] for i in range(len(n)-1)) or all(n[i+1]>n[i] for i in range(len(n)-1))):
            flag=False
        if flag:
            for x in n[1:]:
                if abs(cur-x)<1 or abs(cur-x) >3:
                    flag=False
                    break
                cur=x
        if not flag:
            nn = n.copy()
            for rm in range(len(n)):
                n=nn.copy()
                n.pop(rm)
                cur=n[0]
                flag=True
                if not (all(n[i+1]<n[i] for i in range(len(n)-1)) or all(n[i+1]>n[i] for i in range(len(n)-1))):
                    flag=False
                if flag:
                    for x in n[1:]:
                        if abs(cur-x)<1 or abs(cur-x) >3:
                            flag=False
                            break
                        cur=x
                if flag:
                    break
        ans+=flag
    return ans


if __name__ == '__main__':
    run()
