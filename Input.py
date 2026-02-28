# input() = A function that prompts the user to enter data
#           Returns the entered data as a string
# Strings cannot be used with arithmatic expressions
# Needs to be typecasted to integers or floats

name = input("What is your name?: ")
age = input("How old are you?: ")

# Or can put age = int(input("How old are you?: "))

age = int(age)
age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old.")

