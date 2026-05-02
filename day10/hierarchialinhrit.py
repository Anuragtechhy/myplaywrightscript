class a():
     def __init__(self,name):
         self.name=name

     def naaaam(self,surname):
        print(self.name+surname )


class b(a):
    print("this is b")

class c(a):
    print("this is c")


b1=b('anurag')
c1=c('ram')
b1.naaaam('bhujang')
c1.naaaam('sharma')