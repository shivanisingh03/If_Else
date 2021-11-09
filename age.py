# take a user input of age of 3 people by user and determaine alder people
age=int(input("enter the age of people"))
if age>=50:
    print("oldest")
elif age>=18:
    print("youngest")
elif age>=0:
    print("child")
else:
    print("invalid")