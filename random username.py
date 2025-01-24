import random

def generate_username(adjectives, nouns, include_numbers=False, include_special_chars=False, min_length=6, max_length=12):
    """Generates a random username by combining an adjective and noun.

    Args:
        adjectives (list): List of adjectives.
        nouns (list): List of nouns.
        include_numbers (bool, optional): Whether to include numbers. Defaults to False.
        include_special_chars (bool, optional): Whether to include special characters. Defaults to False.
        min_length (int, optional): Minimum length of the username. Defaults to 6.
        max_length (int, optional): Maximum length of the username. Defaults to 12.

    Returns:
        str: Generated username.
    """

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    if include_numbers:
        num_digits = random.randint(1, 3)
        username += ''.join(random.choice('0123456789') for _ in range(num_digits))

    if include_special_chars:
        num_chars = random.randint(1, 2)
        special_chars = ['!', '@', '#', '$', '%', '&', '*']
        username += ''.join(random.choice(special_chars) for _ in range(num_chars))

    # Adjust length if necessary
    if len(username) < min_length:
        username += ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(min_length - len(username)))
    elif len(username) > max_length:
        username = username[:max_length]

    return username

def main():
    """Main function to get user input and generate usernames."""

    adjectives = ["Cool", "Happy", "Amazing", "Smart", "Funny", "Brave", "Fast", "Strong", "Kind", "Creative"]
    nouns = ["Tiger", "Dragon", "Unicorn", "Eagle", "Lion", "Wolf", "Bear", "Fox", "Cat", "Dog"]

    while True:
        print("\nUsername Generator")
        print("1. Generate Username")
        print("2. Save Usernames to File")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
            min_length = int(input("Minimum username length: "))
            max_length = int(input("Maximum username length: "))

            username = generate_username(adjectives, nouns, include_numbers, include_special_chars, min_length, max_length)
            print("Generated Username:", username)

        elif choice == "2":
            num_usernames = int(input("How many usernames to generate: "))
            filename = input("Enter filename to save to: ")

            with open(filename, 'w') as f:
                for _ in range(num_usernames):
                    username = generate_username(adjectives, nouns, include_numbers, include_special_chars, min_length, max_length)
                    f.write(username + '\n')

            print("Usernames saved to", filename)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()