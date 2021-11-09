print("welcome")
print("IN ICICI BANK")
print("ENTER YOUR CARD")
print("FOR ENGLISH ENETR (1)")
print("FOR HINDI ENETR (2)")
language=int(input(" enetr your language what do you want for english enter 1 and for english enter 2"))
if language==1:
    print("your proccess going in" ,"english")
    pin_code1=int(input("enter your correct in code = "))
    pin_code2=int(input("enter your correct in code = "))
    if pin_code1==pin_code2:
        print("which inquary do you want for that enter this numbers ")
        print("1. cash withdrawal ")
        print("2. balence inquary ")
        print("3. saving ")
        print("4. money transfar ")
        inquary=int(input("enter here which inquary do you want "))
        if inquary==1:
            print("cash withdrawal")
            amount=int(input("enter amount "))
            if amount>=500:
                print(" your transaction is in process ")
                print(" please wait ")
                print("please collect your cash ")
                print("thanks for using icici bank ")
            else:
                print("that note is not abilable ")
        elif inquary==2:
            print("balence inquary")
            print("you have that much money in your account ")
            print("thanks for using icici bank ")
        elif inquary==3:
            print("saving ")
            print("you have saving account ")
            print("thanks for using icici bank ")
        elif inquary==4:
            print("money transfar")
            print("only 500 to more and 10,000 less money transfar ")
            amount=int(input(" enter amount how much money do you want to transfar"))
            if amount>=500 and amount<=10000:
                print(" your money transfar successful ")
            else:
                print("not successful ")
                pin_change=int(input("enter here your new pin code number "))
elif language==2:
    print("aapki prakriya hindi main shuru ho rahi hai ")
    print("aapka suagat hai ")
    print("icici bank main ")        
    pin_code1=int(input("aapna sahi pin code number dale = "))
    pin_code2=int(input("aapna sahi pin code number dale = ")) 
    if pin_code1==pin_code2:
        print("aap kon si jach karna chahate hai ")
        print("1. nakad nikashi  ")
        print("2. rashi ki jach ")
        print("3. bachat khata ")
        print("4. rashi bhejna ")
        jach=int(input("aapko kon si jach karni hai us ke liye upper diye gaye number daliye "))
        if jach==1:
            rakam=int(input("aao kitni rakam nikalna chahate hai "))
            if rakam>=500 and rakam<=10000:
                print("nakad nikashi ")
                print("kriyiya pratiksha kijiye ")
                print("aapki rsksm aa rahi hai ")
                print("kriyipya aapni rakam le lijiye ")
            else:
                print("aapne kahi galti ki hai is liye rakam nhi aa rai hai ")
                print("kripiya fir se koshish kare ")
        elif jach==2:
            print("rashi ki jach ")
            print("aapke khate main abhi itni rashi mojud hai ")
        elif jach==3:
            print("bachat khata ")
            print("aapka ye khata bachat wala hai ")
        elif jach==4:
            print("rashi bhejna ")
            print("aap 500 se uper or 10,000 tak ki rashi bhej sakte hai ")
            rakam2=int(input("aap kitni rakam bhejna chate hai yaha par dale "))
            if rakam2>=500 and rakam2<=10000:
                print("aapki rashi bhej di gai hai ")
            else:
                print("aapki rashi nhi bheji gai ")
else:
    print("dhaniyawad")





