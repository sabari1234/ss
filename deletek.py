from itertools import combinations
Z,K=map(int,input().split())
LIS=len(str(Z))
LIS1=list(combinations(str(Z),LIS-K))
LIS1=sorted(LIS1)
print("".join(LIS1[0]))
