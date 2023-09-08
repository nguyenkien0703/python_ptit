p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    inp=input()
    if inp[0]=="0":
        break
    k,s= inp.split()
    k=int(k)
    res=""
    for i in s:
        # in ra index cua 1 kí tự trong 1 chuoix ở python 
        j=p.find(i)
        # print(j)
        res+=p[(j+k) %28]
    print(res[::-1])