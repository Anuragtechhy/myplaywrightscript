class a():
    def b(self):
        print('This b from class a')

class f(a):

    def b(self):
        super().b()
        print('This is b from class f')


f1=f()
f1.b()
