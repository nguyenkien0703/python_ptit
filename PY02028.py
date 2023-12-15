from math import * 
n , a = int(input()), list(map(int, input().split()))

def nt(n):
    if n<2: return False
    for i in range(2, int(sqrt(n)) +1):
        if n % i== 0:
            return False
    return True


for i in range(n-1):
    if nt(a[i]):
        for j in range(i+1, n):
            if nt(a[j]) and a[i] > a[j]:
                tmp = a[i]
                a[i]=a[j]
                a[j] = tmp
for i in a: print(i, end = ' ')