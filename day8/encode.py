print("WELCOME TO CAESER CIPHER!!!")



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i' ,'j', 
           'k', 'l', 'm', 'n', 'o','p', 'q','r', 's', 't', 'u', 'v', 'x',
           'y','z','a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i' ,'j', 
           'k', 'l', 'm', 'n', 'o','p', 'q','r', 's', 't', 'u', 'v', 'x',
           'y','z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input ("Type your message:\n").lower()
# shift = int( input("Type the shift number:\n"))
    
# making it to accept shift greater than the  number without giving index error

# shift = shift % 26
# def encrypt(plain_text, shift_amount):
#     cipher_text =" "
#     for letter in plain_text:
#         position = alphabet.index(letter)  
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")


# def decrypt(plain_text, shift_amount):
#     cipher_text =" "
#     for letter in plain_text:
#         position = alphabet.index(letter)  
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The decoded text is {cipher_text}")

# if direction == "encode":
#     encrypt(plain_text = text, shift_amount = shift)
# else:
#     decrypt(plain_text = text, shift_amount = shift)


# REORGANIZING THE FUNCTION
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input ("Type your message:\n").lower()
    shift = int( input("Type the shift number:\n"))
#   making it to accept shift greater than the  number without giving index error

    shift = shift % 26

    def caeser(start_text, shift_amount, cipher_direction):
        end_text =" "
        if cipher_direction == "decode":
                shift_amount *= -1
        for char in start_text:
            # making it to allow numbers, symbols and space
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
                
        print(f"The {cipher_direction}d text is {end_text}")
    caeser(start_text= text, shift_amount = shift, cipher_direction = direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye!")

