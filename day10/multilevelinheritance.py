class a():
     def age(self,x):
         print("age is",x)

class b(a):
    def residence(self,reside):
        print("residence is",reside)

class c(b):
    def area(self,area):
        print("area is",area)

c1=c()
c1.age(10)
c1.residence("gwalior")
c1.area("mahrajpura")
c.area('bhopal','indore')
