
from collections import defaultdict


d=open('2025/day5.txt').read().splitlines()

# rs=[]

# i=0
# for l in d:
#     if not l:break
#     a,b=map(int,l.split('-'))
#     rs.append(range(a,b+1))
#     i+=1

# a=0
# for l in d[i+1:]:
#     x=int(l)
#     for v in rs:
#         if x in v:
#             a+=1
#             break
        
# print(a)

s=defaultdict(int)
a=0
for l in d:
    if not l:break    
    a,b=map(int,l.split('-'))
    s[a]+=1
    s[b+1]-=1


# print(s)
c=0
a=0
p=0
for k in sorted(s):
    if c:
        a+=k-p
    c+=s[k]
    p=k

print(a)
