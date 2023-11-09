import math
def chia(n, k):
    if k % 2 == 1:
       return 1;
    ans = 2 ** (n-1)
    if( k == ans ):
        return n 
    if( k < ans ):
        return chia(n-1, k )
    else :
        return chia(n-1, k - ans )



t= int(input())
for k in range(0, t):
    n,k = [int(x) for x in input().split()]
    print(chr(chia(n,k) + ord('A') - 1))