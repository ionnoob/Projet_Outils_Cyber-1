from utils import encrypt, generate_random_key
from vingere import create_table_vigenere

def main():

    print("=== MENU VIGENERE ===")
    print("1) Encrypt a message")
    print("2) Exit")

    choice = int(input("Choose an option : "))

    if choice == "2":
        print("Goodbye!")
        return

    if choice != "1":
        print("Invalid choice.")
        return

    # créé table vignere
    table = create_table_vigenere()

    
    message = input("Enter the message to encrypt : ")

    # Choix clé
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
