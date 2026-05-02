class a():
    def b(self):
        print("this is b from method b")

class c(a):
    def b(self):
        super().b()   # call parent method
        print("this is b from method c")

c1 = c()
c1.b()