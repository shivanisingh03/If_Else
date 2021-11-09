side1=int(input("enter the first angle value"))
side2=int(input("enter the second angle value"))
side3=int(input("enter the thard angle value"))
if side1>side2>side3:
    print(side3,"valid")
elif side2>side3>side1:
    print(side2,"valid")
elif side3>side1>side2:
    print(side3,"valid")
else:
    print("invalid")
