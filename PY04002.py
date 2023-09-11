# chu vi, dieenj tích oop hình chữ nhật 

class Rectangle:
    def __init__(entity,a,b,c):
        entity.a= a
        entity.b= b
        entity.c= c
    def area(entity):
        return entity.a * entity.b  
    def perimeter(entity):
        return (entity.a + entity.b) << 1 
    def color(entity):
        return entity.c[0].upper() + entity.c[1:].lower()
    

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')