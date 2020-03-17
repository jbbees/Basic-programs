# registered to vote.

age = int(input("What is your age? "))
if age < 18:
    print("You are not eligible to vote yet.")
else:
    register = input("Are you registered? (y/n) ")
    if register == 'y' or 'Y':
        print("You are eligible to vote!")
    else:
        print("You need to register in order to vote.")
