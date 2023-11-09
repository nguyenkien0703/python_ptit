n=input()
cnt1=0
cnt2=0
for k in n:
    if k.isupper(): cnt1+=1
    else: cnt2+=1
if cnt1> cnt2:
    print(n.upper())
else:
    print(n.lower())