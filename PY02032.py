s = input()
kien = len(s) //2
cnt = 0
a=[]
i =0
while cnt< kien and i+1 < len(s):
    hoa = s[i] + s[i+1]
    # print(hoa)
    a.append(int(hoa))
    i+=2
c = sorted(a)
b=[]
for i in c:
    if b.count(i)==0: b.append(i)

for i in b:
    print(i,end = ' ')