birth_year=int(input("enter your birth year "))
current_age=int(input("enetr your current age"))
if birth_year<current_age:
    print(current_age-birth_year,"your current age")
elif birth_year>current_age:
    print(birth_year-current_age,"your future age")
else:
    print("invalid")




