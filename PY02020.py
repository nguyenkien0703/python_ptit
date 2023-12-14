from math import * 

n=int(input())
a=sorted([float(x) for x in input().split()])
# tìm max, min nhanh trong 1 mảng 
maxx = max(a)
minn = min(a)
s=0
cntMax=0
cntMin=0
for i in a:
    s+=i
    if i== maxx: cntMax+=1
    if i== minn: cntMin+=1
print("{:.2f}".format((s-cntMax * maxx - cntMin * minn)/(n-cntMax-cntMin)))
