price= {
    '5': 10000,
    '7': 15000,
    '2': 20000,
    '29': 50000,
    '45': 70000,
}
a = {}
# 30F-123.15 Xe_con 5 OUT 06/11/2021

# 30F-123.15 Xe_con 5 IN 06/11/2021

# 30H-123.15 Xe_con 7 IN 06/11/2021

# 29H-222.68 Xe_tai 2 IN 07/11/2021

# 30G-511.15 Xe_con 5 IN 07/11/2021


for i in range(int(input())):
    arr = input().split()
    if arr[-2] == 'OUT': continue
    if a.get(arr[-1]) is None: a[arr[-1]] = price[arr[-3]]
    else: a[arr[-1]] += price[arr[-3]]
for i in sorted(a): print(f'{i}: {a[i]}')