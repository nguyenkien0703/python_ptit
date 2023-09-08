s=input()
# s=s[::-1]
res=""
cnt =0
for i in range(len(s)-3, 0, -3):
    #  lay tu dau den trc ki tu i
    # lay tu ki tu i den cuoi chuoi 
    s=s[:i]+','+s[i:]
print(s)



