from util import encrypt, generate_random_key
from vingere import create_table_vignere

def main():

    print("=== MENU VIGENERE ===")
    print("1) Encrypt a message")
    print("2) Exit")

    choice = input("Choose an option : ").strip()

    if choice == "2":
        print("Goodbye!")
        return

    if choice != "1":
        print("Invalid choice.")
        return

    # Load the Vigenère table
    table = create_table_vignere()

    # Get user message
    message = input("Enter the message to encrypt : ")

    # Ask for key choice
    print("\nKey options:")
    print("1) Enter your own key")
    print("2) Generate a random key")
    key_choice = input("Choose 1 or 2 : ").strip()

    if key_choice == "1":
        key = input("Enter your key (same length as message, letters only) : ")

    elif key_choice == "2":
        key = generate_random_key(message)
        print("Generated key:", key)

    else:
        print("Invalid key option.")
        return

    # Encrypt
    encrypted_msg = encrypt(message, key, table)

    print("\n--- RESULT ---")
    print("Message  :", message)
    print("Key      :", key)
    print("Encrypted:", encrypted_msg)


if __name__ == "__main__":
    main()
