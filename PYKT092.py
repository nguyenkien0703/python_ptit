def cleanName(s):
    return ' '.join([(x[0].upper() + x[1:].lower()) for x in s.split()] )


def checkDT(dt):
    if dt.lower() =='kinh':
        return 0
    return 1.5

def checkKV(n):
    if n== 2:
        return 1
    if n==1 :
        return 1.5
    return 0
class ob:
    def __init__ (self, i, name, diem, dt, kv)-> None:
        self.ID = f'TS{str(i).zfill(2)}'
        self.name = cleanName(name)
        self.diem = diem  + checkKV(kv) + checkDT(dt)
        if self.diem >= 20.5:
            self.type = 'Do'
        else:
            self.type = 'Truot'
    def __str__ (self) -> str:
        return self.ID +" " + self.name+" "+ f'{self.diem:.1f}' +" " + self.type


a=[]
for i in range(int(input())):
    a.append(ob(i+1, input(), float(input()), input(), int(input())))
# a.sort(key =lambda x: -x.diem)
# for i in a: print(i)
for i in sorted(a, key=lambda x: -x.diem): print(i)