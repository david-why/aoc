data=open('2025/day2.txt').read().replace('\n','')
print(data)

ranges=[(int(r.partition('-')[0]), int(r.partition('-')[2])) for r in data.split(',')]

# day1

ans = 0

for r in ranges:
    for x in range(r[0],r[1]+1):
        s=str(x)
        if s[:len(s)//2]==s[len(s)//2:]:
            # print(s)
            ans+=x
print(ans)

# day2

ans = 0

for r in ranges:
    for x in range(r[0],r[1]+1):
        # print(x)
        s=str(x)
        for l in range(2,len(s)+1):# # of sections
            if len(s)%l:continue
            pl=len(s)//l #len of section
            p=s[:pl]
            for d in range(1,l):
                if (s[d*pl:d*pl+pl]!=p):break
            else:
            # if s[:len(s)//2]==s[len(s)//2:]:
                # print(s,l,pl)
                ans+=x
                break
print(ans)
