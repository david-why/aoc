# Advent of Code solution for 2024/9.
from aoc.lib import *

T1 = int
T2 = int

testans1: T1 = None  # type: ignore
testans2: T2 = None  # type: ignore
ans1: T1 = None  # type: ignore
ans2: T2 = None  # type: ignore


def solve1(data: str) -> T1:
    s=list(map(int, list(data.strip())))
    disk=[None] * (sum(s)+1)
    pos=0
    for i in range(len(s)):
        n=s[i]
        if i%2==0:
            for _ in range(n):
                disk[pos]=i//2
                pos+=1
        else:
            pos+=n
            
    print(disk)
    for i in range(len(disk)-1,-1,-1):
        if disk[i] is None:continue
        for j in range(i):
            if disk[j] is not None:continue
            disk[j]=disk[i]
            disk[i]=None
            break
        else:
            break
    print(disk)
    ans=0
    for i in range(len(disk)):
        if disk[i] is not None:
            ans += i*disk[i]
    return ans


def solve2(data: str) -> T2:
    s=list(map(int, list(data.strip())))
    disk:list[int|None]=[None] * (sum(s)+1)
    pos=0
    st={}
    en={}
    le={}
    for i in range(len(s)):
        n=s[i]
        if i%2==0:
            st[i//2]=pos
            for _ in range(n):
                disk[pos]=i//2
                pos+=1
            en[i//2]=pos
            le[i//2]=n
        else:
            pos+=n
    # print(disk)
    for i in range(len(s)//2,-1,-1):
        l=le[i]
        j = 0
        mx=min(len(disk)-l,st[i])
        # find list of Nones at least l long
        while j < mx:
            # print('find',i,j)
            if disk[j] is not None:
                j+=1
                continue
            if all(disk[j+k] is None for k in range(l)):
                break
            j+=1
        else:
            continue
        # move the list
        for k in range(l):
            disk[j+k]=i
        # delete the old list
        for k in range(st[i],en[i]):
            disk[k]=None
    # print(disk)
    ans=0
    for i in range(len(disk)):
        if disk[i] is not None:
            ans += i*disk[i]
    return ans


if __name__ == '__main__':
    run()
