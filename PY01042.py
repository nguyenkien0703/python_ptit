t=int(input())

while t > 0:
    s=input()
    ok =0
    for i in s:
        if i!='0' and i!='1' and i!='2':
            ok=1
            print("NO")
            break
    if ok ==0:
        print("YES")
    t-=1
