from math import *
def nt(n):
    if n<2: return False
    for i in range(2, int(sqrt(n)) +1):
        if n % i== 0:
            return False
    return True




n, a = int(input()), list(map(int, input().split()))
c = []

for i in a:
    if c.count(i) ==  0: c.append(i)
for i in range(1, len(c)):
    c[i] += c[i-1]
ok =0

for i in range(len(c)-1):
    if nt(c[i]) and nt(c[len(c)-1] - c[i]):
        print(i)
        ok=1
        break
if ok == 0:
    print('NOT FOUND')