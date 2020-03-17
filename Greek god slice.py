# Program that asks for user input.
# Get a word or phrase, and 2 numbers.

# Use the 2 numbers to slice the string and print the slice.

uservar = input("Enter the name of a female Greek mythological god. ")
n1 = eval(input("Enter a number. "))
n2 = eval(input("Now enter another number. "))
print(uservar[n1:n2+1])

