def total(n):
    sum =0
    for i in n:
        sum += int(i)
    return sum %10==0

def check(s):
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i-1]))!=2:
            return False
    return True


for t in range(int(input())):
    n=input()
    if( total(n) and check(n)):
        print("YES")
    else:
        print("NO")