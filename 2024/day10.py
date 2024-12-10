# Advent of Code solution for 2024/10.
from aoc.lib import *

T1 = int
T2 = int

testans1: T1 = None  # type: ignore
testans2: T2 = None  # type: ignore
ans1: T1 = None  # type: ignore
ans2: T2 = None  # type: ignore


def solve1(data: str) -> T1:
    n,d=spl(data)
    m=len(d[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if d[i][j]!='0': continue
            ans += bfs1(d,i,j)
    return ans


def bfs1(d,i,j):
    n=len(d)
    m=len(d[0])
    q=[(i,j)]
    st=set()
    anss=set()
    while q:
        i,j=q.pop()
        c=d[i][j]
        for mx,my in [(0,1),(1,0),(0,-1),(-1,0)]:
            x,y=i+mx,j+my
            if x<0 or y<0 or x>=n or y>=m or d[x][y]!=str(int(c)+1) or (x,y) in st: continue
            if d[x][y]=='9':
                anss.add((x,y))
            else:
                q.append((x,y))
                st.add((x,y))
    return len(anss)


def solve2(data: str) -> T2:
    n,d=spl(data)
    m=len(d[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if d[i][j]!='0': continue
            ans += bfs2(d,i,j)
    return ans

def bfs2(d,i,j):
    n=len(d)
    m=len(d[0])
    q=[(i,j,())]
    st=set()
    anss=set()
    while q:
        i,j,pt=q.pop()
        c=d[i][j]
        for mx,my in [(0,1),(1,0),(0,-1),(-1,0)]:
            x,y,pt2=i+mx,j+my,pt+((i,j),)
            if x<0 or y<0 or x>=n or y>=m or d[x][y]!=str(int(c)+1) or (x,y,pt2) in st: continue
            if d[x][y]=='9':
                anss.add((x,y,pt2))
            else:
                q.append((x,y,pt2))
                st.add((x,y,pt2))
    return len(anss)


if __name__ == '__main__':
    run()
