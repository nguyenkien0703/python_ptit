t=int(input())
for k in range(t):
    n=input()
    first1=str(n)[0:2:]
    cuoi1= str(n)[-2::]
    print(first1)
    print(cuoi1)
    if first1== cuoi1:
        print("YES")
    else: print("NO")
    print()