n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))

l =[]
for i in arr:
    if i not in l:
        l.append(i)

l.sort()
n=len(l)
a=[]

def Try(i):
    if len(a) == k:
        for i in a:
            print(i,end=' ')
        print()
        return 

    for i in range(i, len(l)):
        a.append(l[i])
        Try(i+1)
        # xoá phân tử cuối mảng 
        a.pop()

Try(0)