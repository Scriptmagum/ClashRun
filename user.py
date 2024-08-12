a,s=input().split()
a=float(a)
d={"thousand":1000,"hundred":100,"million":1000000}
print(int(a*d[s]))