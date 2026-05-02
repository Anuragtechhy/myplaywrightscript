list1=[10,20,30,'Anurag']
print(id(list1))

list1[0]='9990'
list1=[list1[0]]+list1[1:]
print(id(list1))

print(list1[3])

for i in list1:
    print(i)

if '9990' in list1:
    print("9990 exists")

mylist=list1.copy()
print(mylist)