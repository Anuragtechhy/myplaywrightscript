mydisc={

    "name":"anurag",
    "age":35,
     "surname":"bhujang"
}

print(mydisc)

# mydisc1=dict(name="anurag",age=35,surname="bhujang")
# print(mydisc1)

mydisc2=mydisc.get("name")
print(mydisc2)

print(mydisc.keys())
print(mydisc.items())
print(mydisc.values())
mydisc.update({"age":32})
print(mydisc)