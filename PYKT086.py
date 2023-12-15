from math import * 
c = ['A','B','C','D','E','F']
f = open('DATA.in', 'r')
t = f.readline()
while(t> 0):
    n= int(f.readline())
    s = f.readline()
    b = int(log(n, 2))
    if n==2:
        print(s)
        t-=1
        continue
    while len(s)% b !=0:
        s = "0" + s 
    i = 0
    while i < len(s):
        tmp = 0
        for j in range(i, i + b):
            tmp += int(s[j]) * (2**(b-j+i-1))
        if tmp < 10:
            print(tmp, end ='')
        else:
            print(c[tmp - 10], end = '')
        i+=b
    print()
    t-=1


