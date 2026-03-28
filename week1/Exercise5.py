name=input("Enter your name:")
if len(name)< 3:
    print("Must be atleast 3 characters")
elif len(name)> 50:
    print("Cannot exceed 50 characters")
else:
    print("Name looks good!")

