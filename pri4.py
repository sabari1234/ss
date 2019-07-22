s,d=map(str,input().split())
f=0
if len(s)>len(d):
    s,d=d,s
d1=0
while d1<len(s):
      f+=(ord(d[d1])-ord(s[d1]))
      d1+=1
for d1 in range(d1,len(d)):
      f+=ord(d[d1])-ord('a')+1
print(f)
