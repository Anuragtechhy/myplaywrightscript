mylist1=[10,23,30,'anurag',True]
print(mylist1)

mylist2=mylist1.copy()
print(mylist2)
print(id(mylist2))
print(mylist2.clear())

mylist1.append("False")
print(mylist1)
mylist1.insert(2,50)
print(mylist1)
mylist1.pop(1)
print(mylist1)

for a in mylist1:
    print(a)

    mylist3=list()
    print(mylist3)