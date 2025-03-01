import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Password should be at least 4 characters long.")
    else:
        password = generate_password(length)
        print(f"Generated Password: {password}")

except ValueError:
    print("Invalid input. Please enter a number.")
