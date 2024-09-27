
import random
import string

def password_generator(length, complexity):
    characters = ''
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters
    elif complexity == 3:
        characters = string.ascii_letters + string.digits
    elif complexity == 4:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter password length (min 8): "))
    while length < 8:
        print("Password length should be at least 8.")
        length = int(input("Enter password length: "))

    print("Select complexity level:")
    print("1. Lowercase letters")
    print("2. Mixed case letters")
    print("3. Letters and numbers")
    print("4. Letters, numbers, and special characters")
    complexity = int(input("Enter complexity level (1-4): "))
    while complexity < 1 or complexity > 4:
        print("Invalid complexity level. Please choose between 1 and 4.")
        complexity = int(input("Enter complexity level: "))

    password = password_generator(length, complexity)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()

