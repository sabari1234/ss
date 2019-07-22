a,b=input().split()
o=abs(len(a)-len(b))
for j in range(len(a)):
    if len(b)==1 and a[j] in a:
        break
    if a[j]!=b[j]:
        o+=1
print(o)
