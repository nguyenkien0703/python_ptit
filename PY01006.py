
def check(n):
    for x in n:
        if x!='4' and  x!='7':
            return False
    return True


t=int(input())
for k in range(t):
    n=input()
    if check(n): print("YES")
    else: print("NO")        