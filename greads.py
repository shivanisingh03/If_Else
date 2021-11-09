subject1=int(input("enter your physics marks "))
subject2=int(input("enter your chemistry marks "))
subject3=int(input("enter your biology marks "))
subject4=int(input("enter your mathametics marks "))
subject5=int(input("enter your computer marks "))
sum=(subject1+subject2+subject3+subject4+subject5)
percentage=(sum/500*100)
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=70:
    print("Grade C")
elif percentage>=60:
    print("Grade D")
elif percentage>=40:
    print("Grade E")
elif percentage<=40:
    print("Grade F")