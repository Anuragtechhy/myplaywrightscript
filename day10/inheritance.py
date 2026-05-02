class a():
    x = int(input("enter first number :"))
    y = int(input("enter second number :"))

    def anu(self, a, b):
        print(a + b + self.x + self.y)

    @staticmethod
    def bhu(cls, c, d):
        print(c + d + cls+a.x)


class b(a):
    def __init__(self, f):
        self.f = f


b1 = b(23)

a.bhu(34, 45,67)
b1.anu(23,32)

print(b1.f)