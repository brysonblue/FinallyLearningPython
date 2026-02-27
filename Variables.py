# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains
# F-strings, or formatted string literals, are a Python feature (introduced in 3.6)
# used for cleaner, faster, and more readable string formatting by prefixing a string with f or F.
# They allow you to directly embed variables, objects, or expressions inside curly braces {} within a string, which are evaluated at runtime.
# Strings, strings are text

first_name = "Bro"
food = "pizza"
email = "Bro123@fake.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")

# Integers, integers are whole numbers
age = 27
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You have {quantity} classes")
print(f"Your class has {num_of_students} students")

# Float, floats are decimal numbers
price = 10.99
gpa = 4.00
distance = 5.5

print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance} Kilometers")

# Boolean, boolean are true/false, usually 1 for true, 0 for false

# is_student = True

# if is_student:
#    print(f"You are a student")
# else:
#    print(f"You are NOT a student")

# Print(f"Are you a student?: {is_student}")

is_student = False
for_sale = True
is_online = True

if for_sale:
    print(f"That item is for sale")
else:
    print(f"That item is NOT for sale")

if is_online:
    print(f"You are online")
else:
    print(f"You are offline")
