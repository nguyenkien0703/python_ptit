n, a = int(input()), list(map(int, input().split()))
a.sort()
print(max({a[-3] * a[-2] * a[-1], a[0] * a[1] * a[-1], a[0] * a[1] * a[2]}))