d=open('2025/day4.txt').read().splitlines()

g=lambda x,y:'.' if x<0 or y<0 or x>=len(d[0]) or y>=len(d) else d[y][x]

# a=0
# for x in range(len(d[0])):
#     for y in range(len(d)):
#         c=0
#         for gx in range(-1,2):
#             for gy in range(-1,2):
#                 c += g(x+gx,y+gy)=='@'
#         if c<=4 and g(x,y)=='@':
#             a+=1

# print(a)

a=0
t=True
while t:
    t=False
    for x in range(len(d[0])):
        for y in range(len(d)):
            c=0
            for gx in range(-1,2):
                for gy in range(-1,2):
                    c += g(x+gx,y+gy)=='@'
            if c<=4 and g(x,y)=='@':
                d[y] = d[y][:x]+'.' + d[y][x+1:]
                t=True
                a+=1
print(a)
