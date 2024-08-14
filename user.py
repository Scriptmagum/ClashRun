*m,=map(int,input().split())
p=[]
n=[]
for a in m:
    if a<0:n+=[a]
    else:p+=[a]
s=sum(n)
for x in p:
    if -x not in n:s+=x
print(s)