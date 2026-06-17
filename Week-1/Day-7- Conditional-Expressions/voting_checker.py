age = int(input("Enter your age: "))

if age < 0:
    print("Invalid Age")
elif age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
