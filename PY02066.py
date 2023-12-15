# kien
#  xu ly nang cao, tren nhieu dong

n = input()
a =[]
while True:
    try:
        arr = list(map(int, input().split()))
        a.extend(arr)
    except: break
a.sort()
r = a[-1]
mp ={}
for i in a:
    if mp.get(i) is None: mp[i]=1
ok = 0
for i in range(1, r+1):
    if mp.get(i) is None:
        ok = 1
        print(i)
if ok ==0:
    print('Excellent!')
