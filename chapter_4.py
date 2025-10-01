cup = input("Enter the cup size (small, medium, large): ")
if cup == "small":
    price = 2.50
elif cup == "medium":
    price = 3.00
elif cup == "large":
    price = 3.50
else:
    price = 0.00
    print("Invalid cup size entered.")