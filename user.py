s=input()
v=1
c=""
for a in s:
    if a.isalpha():
        if v:c+=a.lower();v=0
        else:c+=a.upper();v=1
    else:
        c+=a
print(c)

