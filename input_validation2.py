# Koen K. & Arden
# DEC 10 2024
# Validating String Input (Level 2)

user_input = input("Please enter a number that is 5 or more characters: ")

if user_input.isdigit() and len(user_input) >= 5:
    print(f"Valid numeric input with enough length: {user_input}.")
elif not user_input.isdigit():
    print("Input must be a number.")
else:
    print("Input must be at least 5 characters long.")