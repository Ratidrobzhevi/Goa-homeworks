
lastname = input("Enter your lastname")

if lastname[0].lower() == "m":
    print(lastname.upper())
elif lastname[0].lower() == "g":
    print(lastname.lower())
else:
    print("არ იწყება არც m და არც g ასოთი.")
