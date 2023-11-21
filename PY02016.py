for t in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    # su dung map trong py
    myMap={}
    fMax = 1
    num = int(1e7)
    for i in a:
        if i not in myMap:
            myMap[i]=1
        else:
            myMap[i]+=1
    fMax = max(myMap.values());
    for k, h in myMap.items():
        if h == fMax:
            fMax= h
            num= min(num, k)
    if (fMax > n//2):
        print(num)
    else:
        print("NO")