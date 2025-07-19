import random
import string

def generate_password(length):
    # Define the characters to use: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random choices
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!")

    try:
        # Ask user for the desired password length
        length = int(input("Enter the desired password length: "))

        if length <= 0:
            print("❌ Password length must be greater than 0.")
            return

        # Generate and display the password
        password = generate_password(length)
        print(f"\n✅ Your generated password is:\n{password}")
    
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

# Run the program
main()
