num=int(input("enter the number "))
if num%2==0:
    print("not weird ")
    if num%2!=0:
        if num>2 and num<5:
            print("werid ")
        else:
            print("not ")
else:
    print("wrong number ")