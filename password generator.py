import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    password = []
    char_sets = []

    if use_uppercase:
        char_sets.append(string.ascii_uppercase)
    if use_lowercase:
        char_sets.append(string.ascii_lowercase)
    if use_numbers:
        char_sets.append(string.digits)
    if use_special_chars:
        char_sets.append(string.punctuation)

    # Ensure at least one character from each selected character set
    for char_set in char_sets:
        password.append(random.choice(char_set))

    # Fill the rest of the password with random characters from all selected sets
    for _ in range(length - len(char_sets)):
        password.append(random.choice(''.join(char_sets)))

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Password Generator")
    print("------------------")

    length = int(input("Enter the desired password length: "))

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)

    print("Generated Password:", password)

if __name__ == "__main__":
    main()