from math import * 
def tn(x):
    s = str(x)
    daonguoc = s[::-1]
    if len(s) <=1: return False
    return daonguoc == s 

n, m = map(int,input().split())
a=[]
for i in range(n):
    a.append([int(x) for x in input().split()])
ans = []
ok = 0
Max = 0
for i in range(n):
    for j in range(m):
        if tn(a[i][j]) == True: 
            Max = max(Max, a[i][j])
            ok = 1
if ok ==0:
    print('NOT FOUND')
else:
    for i in range(n):
        for j in range(m):
            if a[i][j] == Max: 
                # print(f'vi tri [{i}][{j}] la : {a[i][j]}')
                ans.append(f'Vi tri [{i}][{j}]')


    print(Max)
    for i in ans:
        print(i)