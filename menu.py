from utils import *
from vigenere import create_table_vigenere
from file_manager import *


def main():

    print("=== MENU VIGENERE ===")
    print("1) Encrypt a message")
    print("2) Decrypt a message")
    print("3) Frequence Table(File reccomended for better result)")
    print("4) Exit")

    choice = int(input("Choose an option : "))

    if choice == 4:
        print("Goodbye!")
        return

    if choice != 1 and choice != 2 and choice != 3:
        print("Invalid choice.")
        return

    if choice == 3:
        print("\nChoice File or Text")
        print("1) From File")
        print("2) From text")
        is_file = int(input("Choose 1 or 2 : "))

        if is_file==1:
            filename= input("Enter Your file name (.txt) : ").strip()
            output = input("Enter your output file name (.txt) : ").strip()
            if output=="":
                tab_rec(filename, from_file=True)
            else:
                tab_rec(filename, from_file=True,output_file=output)
        elif is_file == 2:
            text = input("Enter your message : ").strip()
            output = input("Enter your output file name (.txt) : ").strip()
            if output == "":
                tab_rec(text)
            else:
                tab_rec(text,output_file=output)
        else:
            print("Invalid choice.")
        return


    # créé table vignere
    table = create_table_vigenere()

    # --------------------------------------------------
    # Choix source du message
    # --------------------------------------------------
    print("\nMessage source:")
    print("1) Enter message manually")
    print("2) Load message from file")

    source_choice = int(input("Choose 1 or 2 : "))

    if source_choice == 1:
        message = input("Enter the message : ")

    elif source_choice == 2:
        file_path = ask_file_path()
        message = read_file(file_path)

    else:
        print("Invalid source option.")
        return

    # --------------------------------------------------
    # ENCRYPTION
    # --------------------------------------------------
    if choice == 1:

        # Choix clé
        print("\nKey options:")
        print("1) Enter your own key")
        print("2) Generate a random key")
        key_choice = int(input("Choose 1 or 2 : "))

        if key_choice == 1:
            key = input("Enter your key (same length as message, letters only) : ")

        elif key_choice == 2:
            key = generate_random_key(message)
            print("Generated key:", key)

        else:
            print("Invalid key option.")
            return

        # Encrypt
        encrypted_msg = encrypt(message, key, table)

        print("\nKey options:")
        print("1) Save key to a file")
        print("2) Do not save key")

        key_save_choice = int(input("Choose 1 or 2 : "))

        if key_save_choice == 1:
            save_key_to_file(key)



        print("\nOutput options:")
        print("1) Display result on screen")
        print("2) Save result to file")

        output_choice = int(input("Choose 1 or 2 : "))

        if output_choice == 1:
            print("\n--- RESULT ---")
            print("Message  :", message)
            print("Key      :", key)
            print("Encrypted:", encrypted_msg)

        elif output_choice == 2:
            output_file = save_as("encrypted.txt")
            write_file(output_file, encrypted_msg)

        else:
            print("Invalid output option.")
            return







    # --------------------------------------------------
    # DECRYPTION
    # --------------------------------------------------
    if choice == 2:

        print("\nKey source:")
        print("1) Enter key manually")
        print("2) Load key from file")

        key_source = int(input("Choose 1 or 2 : "))

        if key_source == 1:
            key = input("Enter your key : ").strip()

        elif key_source == 2:
            key = load_key_from_file()

        else:
            print("Invalid key option.")
            return


        decrypt_msg = decrypt(message, key, table)

        
        print("\nOutput options:")
        print("1) Display result on screen")
        print("2) Save result to file")

        output_choice = int(input("Choose 1 or 2 : "))

        if output_choice == 1:
            print("\n--- RESULT ---")
            print("Message  :", message)
            print("Key      :", key)
            print("Decrypted:", decrypt_msg)

        elif output_choice == 2:
            output_file = save_as("decrypted.txt")
            write_file(output_file, decrypt_msg)

        else:
            print("Invalid output option.")
            return


if __name__ == "__main__":
    main()
