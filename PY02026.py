n,  m = [int(x) for x in input().split()]
a= sorted(set(map(int, input().split())))
b= sorted(set(map(int, input().split())))
if a== b:
    print("YES")
else: print('NO')