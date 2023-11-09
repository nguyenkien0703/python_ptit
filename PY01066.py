t=int(input())

def solve(s):
    s=s
    rev_s = s[::-1]
    ok =0;
    for i in range(1,len(s)):
        # ord: lấy ra số của mã ascil của kí tự 
        if (abs(ord(s[i]) - ord(s[i-1])) ) != (abs(ord(rev_s[i]) - ord(rev_s[i-1])) ):
            ok =1;
            print("NO")
            return

    if ok == 0:
        print("YES")

while t > 0:
    s=input()
    solve(s)
    t-=1