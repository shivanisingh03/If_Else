age=int(input("enter the age "))
sex=input(" enter male(m) or female (f) ")
marital_status=input("enter status yes(y) or no(n) ")
if sex=="f" and marital_status=="y":
    print("she will work only urbn area")
    if age>=20 and age<=40:
        print("work in urbn area")
    else:
        print("work in urbn area")
elif sex=="m" and marital_status=="n":
    print("he will work only urban area ")
    if age>=40 and age>=60:
        print("work in urban")
    else:
        print("work in urban")
else:
    print("they was other gender")