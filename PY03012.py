#  đối tượng trong python 


class student:
    def __init__(person, ten,dung, tong):
        person.ten = ten
        person.dung= dung
        person.tong = tong

a=[]
for z in range(int(input())):
    x=input()
    y,z = map(int, input().split())
    a.append(student(x,y,z))
# sắp xếp đối tượng trong python 
a.sort(key=lambda i : ((-1) * i.dung, i.tong, i.ten))

for i in a:
    print('{} {} {}'.format(i.ten,i.dung,i.tong))


