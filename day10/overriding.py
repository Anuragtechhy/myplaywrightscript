class a():
    def b(self):
        print("This is b from class a")

class b(a):
    def b(self):
        print("This is b from class b")
        super().b()

b1 = b()
b1.b()