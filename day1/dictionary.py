def a(x,y):
    print(x+y)
a(100,200)


class b:
    def c(self,d,e,f):
        print(d,e,f)

b1=b()
b1.c(32,f=98,e=32)



# def n(k,l):
#     if (k>l):
#         return l,k
#     else:
#         return k,l
#     v=n(50,98)
#     print(v)

def n(k, l):
    if k > l:
        return l, k
    else:
        return k, l


v = n(50, 98)
print(v)