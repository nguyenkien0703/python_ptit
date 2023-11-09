#  chia ra thành mảng các só gnuyeen từ cách nhập 
x = 0
b = [0] * 42
while True :
    a = [int(x) for x in input().split()]
    x += len(a)
    s = 0
    for i in a :
        b[i % 42] = 1
    if x == 10 : break
for i in b :
    #  nếu i =0 thì là chia hetes, k dc gọi là chia dư nữa
    if i>0: s += 1
print(s)