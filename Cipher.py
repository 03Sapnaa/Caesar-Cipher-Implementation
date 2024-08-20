import string

# Function to encrypt the plaintext
def encrypt(plaintext, shift):
    encrypted_text = []
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            encrypted_text.append(new_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

# Function to decrypt the ciphertext
def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

# Function to perform a brute-force attack
def brute_force_attack(ciphertext):
    possible_texts = {}
    for shift in range(26):
        decrypted_text = decrypt(ciphertext, shift)
        possible_texts[shift] = decrypted_text
        print(f'Shift {shift}: {decrypted_text}')
    return possible_texts

# Function to perform frequency analysis (basic)
def frequency_analysis(ciphertext):
    freq_dict = {}
    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    sorted_freq = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_freq

# Command-Line Interface
def cli():
    print("Welcome to the Caesar Cipher Program")
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Brute Force Attack")
        print("4. Frequency Analysis")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            shift = int(input("Enter the shift value: "))
            ciphertext = encrypt(plaintext, shift)
            print(f"Encrypted text: {ciphertext}")
        
        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            shift = int(input("Enter the shift value: "))
            plaintext = decrypt(ciphertext, shift)
            print(f"Decrypted text: {plaintext}")
        
        elif choice == '3':
            ciphertext = input("Enter the ciphertext: ")
            print("Brute Force Attack Results:")
            brute_force_attack(ciphertext)
        
        elif choice == '4':
            ciphertext = input("Enter the ciphertext: ")
            freq_analysis = frequency_analysis(ciphertext)
            print("Frequency Analysis:")
            for char, freq in freq_analysis.items():
                print(f"{char}: {freq}")
        
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cli()
