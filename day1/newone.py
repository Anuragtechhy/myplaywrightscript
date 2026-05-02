amount=int(input("enter amount"))
# discount=int(input("enter discount"));

if amount<=1000:
    discount=amount*20/100
    print("new amount is :",amount-discount)

elif  amount>1000 and   amount<5000:
    discount = amount * 10 / 100
    print("new amount is :", amount - discount)

else:
    print("not eligible for any discount")



