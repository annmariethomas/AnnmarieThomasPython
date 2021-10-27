print(" ------------------------------------------------") 
print("|                                                |")
print("|    06whileLoop                                 |")
print("|    Name : Annmarie Thomas                      |") 
print("|    Version : 01                                |")
print("|                                                |")
print(" ------------------------------------------------")
ans = input("What is the name of the subject ")
while ans != ("IST"):
    print("Not correct - try again")
    ans = input("What is the name of the subject ")
    continue
else:
    print("\nCongratulations!!")
