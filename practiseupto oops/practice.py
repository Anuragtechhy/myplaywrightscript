# Inheritance and polymorphism

class myclass:
    x=int(input(" enter class level variable first value: "))
    y=int(input(" enter class level variable second value: "))
    def a(self):
        a1=10
        b=20
        print(a1+b)
        print(self.y+self.x)
print('a','b')


class myclassb(myclass):
    def b(self):
        c=21
        d=34
        print(c+d)


class myclassc(myclass):
    def c(self,f,g):
        print(f+g)


m1=myclassb()
m2=myclassc()
m1.a()
m1.b()
print(m1.y)
m2.c(12,34)
print(m2.x)
print(m2.a)







