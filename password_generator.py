import random

def generate_password(length, is_random_subs, is_random_caps):
    """
    Generates a password based on the given length and mode.

    Parameters:
        length (int): The number of characters in the password.
        is_random_subs (str): "1" for yes to swapping, "2" for no to swapping.
        is_random_caps (str): "1" for yes to capitalization, "2" for no to capitalization.

    Returns:
        str: The generated password.
    """

    substitution_map = {
        'a': '@', 'b': '8', 'e': '3', 'g': '9', 'i': '1', 'l': '1', 'o': '0', 's': '$', 't': '+', 'z': '2',
        'A': '4', 'B': '8', 'E': '3', 'G': '6', 'I': '!', 'O': '0', 'S': '$', 'T': '7', 'Z': '2'
    }

    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Generate an easy-to-say password
    password = ""
    consonant_toggle = True
    while len(password) < length:
        if consonant_toggle:
            password += random.choice(consonants)
            consonant_toggle = False
        else:
            password += random.choice(vowels)
            consonant_toggle = True

    # Randomly substitute characters to uppercase
    if is_random_caps == "1":
        password = ''.join(c.upper() if random.random() < 0.5 else c for c in password)

    # Randomly substitute characters based on the substitution map
    if is_random_subs == "1":
        password = ''.join(substitution_map.get(c, c) if random.random() < 0.3 else c for c in password)

    return password

# Example usage
if __name__ == "__main__":
    try:
        length = int(input("Enter the number of characters for the password: "))
        is_random_subs = int(input ("Do you want to substitute random characters with similar looking symbols and numbers? (1:yes, 2:no): "))
        if is_random_subs!= 1 or is_random_subs!= 2:
            raise ValueError()
        
        is_random_caps = int(input("Do you want to randomly capitalize characters? (1:yes, 2:no): "))
        if is_random_caps!= 1 or is_random_caps!= 2:
            raise ValueError()

        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            password = generate_password(length, is_random_subs, is_random_caps)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
