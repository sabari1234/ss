b=int(input())
d=[]
for i in range(0,b):
 s=input()
 d.append(s)
l=[]
for i in zip(*d):
    if(i.count(i[0])==len(i)):
        l.append(i[0])
    else:
     break
print(''.join(l))
