data=open('2025/day3.txt').read().splitlines()

# p 1

a=0

for l in data:
    s=l[:-1]
    d=-1
    p=0
    for i,x in enumerate(s):
        if int(x)>d:
            d=int(x)
            p=i
    d2=int(max(l[p+1:]))
    num=int(f'{d}{d2}')
    a+=num

print(a)


# p 1

a=0

def f(s,d):
    # find d digits in s
    if d==0:return ''
    if len(s)<d: return ''
    z=s[:len(s)-d+1]
    v=0
    p=0
    for i,x in enumerate(z):
        if int(x)>v:
            v=int(x)
            p=i
    return (f'{v}{f(s[p+1:],d-1)}')

a=0
for l in data:
    a+=int(f(l,12))

print(a)
