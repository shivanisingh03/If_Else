# write a c program to check whether a cheracter is alphabetor not
character=input("enter your character")
if character>="a" and character<="z":
    print(character,"it is a small alphabet")
elif character>="A" and character<="Z":
    print(character,"it is a capital alphabet")
else:
    print("nothing ")