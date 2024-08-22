a,b,c,d=map(int,input().split())
i=a
j=0
for _ in range(a-b+1):
    print(i)
    i+=c
    if j==d:i=a;j=0
    j+=1