for t in range(int(input())):
    n, a = int(input()), [int(x) for x in input().split()]
#  su dung map trong py de hon 
    m={}
    for i in a:
        if m.get(i) is None: m[i]= 1
        else : m[i]+=1
    for i in m:
        if m[i]%2==1:
            print(i)
            break;