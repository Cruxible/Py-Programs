def encrypt():
    # Step 1 - Get input

    plaintext = input("Enter pharse to be encrypted: ")

    # Step 2 - Process input

    cipher_text = ""

    for letter in plaintext: 
        letter_code = ord(letter)

        new_letter_code = letter_code + 3000

        new_letter = chr(new_letter_code)

        cipher_text += new_letter

    # Step 3 - Output result

    print(cipher_text)

def decrypt():
    # Step 1 - Get input

    plaintext = input("Enter pharse to be encrypted")

    # Step 2 - Process input
    cipher_text = ""

    for letter in plaintext: 
        letter_code = ord(letter)

        new_letter_code = letter_code - 3000

        new_letter = chr(new_letter_code)

        cipher_text += new_letter

    # Step 3 - Output result
    print("xxxxXXXXxxxx")
    print(cipher_text)
    print("xxxxXXXXxxxx")

def displayMenu():
    print("===========================")
    print("would you like to either:: ")
    print("1. Encrypt                 ")
    print("2. Decrypt                 ")
    print("3. Exit                    ")
    print("===========================")
    choice = input("Type Number Of Your Choice: ")
    if choice == "1" or choice == "2" or choice == "3" :
        return choice
    else:
        print("Invalid choice, please try again/n/n/n")
        return False

def main():
    running = True
    while running:
        choice = displayMenu()
        if choice == "1":
            encrypt()
        elif choice == "2":
            decrypt()
        elif choice == False:
            continue
        elif choice == "3":
            print("Exiting")
            break

main()
