n=int(input())
a=[int(x) for x in input().split()]
b=[0] * 30001
minn = 30004
maxx = 0
for i in a:
    if i  > maxx: maxx=i
    if i < minn: minn=i
    b[i]=1
for i in range(minn, maxx + 2):
    if b[i]==0:
        print(i);
        break