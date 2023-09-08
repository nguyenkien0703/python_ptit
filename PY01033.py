from math import * 
a,b =[int(x) for x in input().split()]  
for i in range(a,b-1):
    for j in range(i+1, b):
        for k in range(j+1,b+1):
            if gcd(i,j)==1 and gcd(j,k)==1 and gcd(i,k)==1:
                print('({}, {}, {})'.format(i,j,k))





    # 1-> 4
    # 1 2 3 
    #5,1,-1
    # 5 4 3 2 