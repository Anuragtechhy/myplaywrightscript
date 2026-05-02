a = "anurag"
# b = 10
# # print(a + "\n" + b)
#
# # slicing of strings
#
#
# print(a[1:-2])
# c=f"name is {a} and age is {b}"
# print(c)

print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.casefold())
print(a.center(10,"*"))
print(a.find("r"))
print(a.count("a"))

b="23.90"
print(b.isdecimal())
print(b.isnumeric())


c="anuragbhujang@gmail.com"
print(c.split("."))
print(c[3])

print(id(c))


c="A"+c[0:]
print(id(c))