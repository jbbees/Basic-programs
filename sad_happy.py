from sys import argv

# sad happy program. pass sad :( and change to happy :)

script, feeling = argv

prompt = '> '    # this is just a variable called prompt that we'll at the input stage.
                 # having a space just makes the input area start a space away from the > on the input line.

print(f"Loading {script}...")
print(f"You enteted {feeling} on the command line :( ")

print("Enter \"happy\" at the '>' to change the way you feel right now that you're coding in Python.")
feeling = input(prompt)

print(f"You have entered {feeling} :) ")
