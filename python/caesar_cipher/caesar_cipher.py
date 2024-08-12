from art import logo
print (logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for item in original_text:
        if item not in alphabet:
            output_text += item
        elif item in alphabet:
            index_value = alphabet.index(item)
            if encode_or_decode == "decode":
                x = shift_amount * - 1
                index_value += x
            else:
                index_value += shift_amount
            index_value %= len(alphabet)
            output_text += alphabet[index_value]
    print(f"Here is the {encode_or_decode}d letter : {output_text}")



# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
#
#
# cipher = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
# while cipher == "yes":
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#
#     caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

continue_cipher = True

while continue_cipher :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    cipher = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if cipher == "no":
        continue_cipher = False