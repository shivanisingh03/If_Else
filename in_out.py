girls=int(input("enter the girls quantity"))
if girls==12:
    print(girls,"room is ocupied")
elif girls<12:
    print(12-girls,"bad are left")
elif girls>12:
    print(girls-12,"that girls shift in other room ")
else:
    print("invalid")