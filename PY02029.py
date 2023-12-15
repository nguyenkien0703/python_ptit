n, m = map(int, input().split())
a = list(map(int, input().split()))
mp ={}
for i in a:
    if mp.get(i) is None: mp[i] =1 
    else: mp[i] += 1
a = sorted(a, key = lambda x: (-mp.get(x), x ))
Max = mp[a[0]]
# print(a)
#  a.pop(0) la loai bo phan tu dau tien cua a 
# a.pop() la loai bo phan tu cuoi cung cua mang a 
while len(a) > 0 and mp[a[0]] == Max: a.pop(0)
# print(a)
if len(a) == 0: print('NONE')
else: print(a[0])
