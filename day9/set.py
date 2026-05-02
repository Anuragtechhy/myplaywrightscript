myset1={1,2,3,4,'anurag'}
print(myset1)

myset2=myset1.copy()
print(myset2)

myset2.add("bhujang")
print(myset2)

myset2.remove("bhujang")
print(myset2)
myset2.pop()
print(myset2)

myset3=myset1.intersection(myset2)
print(myset3)