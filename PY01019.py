t=int(input())

def solve(s):
    s=s
    rev_s =s[::-1]
    l = len(s)
    for i in range(1,l):
        # hàm ord() trả về mã ascil của kí tự 
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(rev_s[i])-ord(rev_s[i-1])):
            print("NO")
            return
    print("YES")




while t > 0:
    s=input()
    solve(s)
    t-=1