num=int(input("enter the number "))
num1=num%10
num2=(num//10)%10
num3=(num//100)%10
num4=(num//1000)%100
new_no=((num1*1000)+(num2*100)+(num3*10)+(num4*1))
if num<=10000:
    print(new_no)
else:
    print("it is not reverse")



