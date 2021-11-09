side1=int(input("enter the first angle value"))
side2=int(input("enter the second angle value"))
side3=int(input("enter the thard angle value"))
if side1==side2==side3:
    print("trianle is eqailateral")
elif side1==side2 or side1==side3 or side2==side3:
    print("triange is isosceles")
else:
    print("it is scalene")