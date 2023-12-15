
def solve():
    n=input()
    cnt = 0
    if len(n) <= 1:
        print(1)
        return 
    while len(n) !=1:
        total = 0
        cnt +=1
        for i in n:
            total += (ord(i)- 48)
        n = str(total)
    print(cnt)


t=1 
while t > 0:
    solve()
    t-=1