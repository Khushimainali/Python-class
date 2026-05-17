
name = input("Enter name : ")
age = int(input("Enter age : "))
eligible = input("Are you citizen (y/n) :")

if age>=18 and eligible == "y":
    print("Eligible to vote")
elif age>=18 and eligible == "n":
    print("Not eligible to vote")
else:
    print("To young to vote")