alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(plain_text,shift_amount):
    cipher_text="";
    for letter in plain_text:
      current_position=alphabet.index(letter)
      new_position_after_shift=current_position+shift_amount
      cipher_text+=alphabet[new_position_after_shift]
    print(f"The encoded text is {cipher_text}")

def decrypt (cipher_text,shift_amount):
    plain_text=''
    for letter in cipher_text:
      current_position=alphabet.index(letter)
      new_position_after_shift=current_position-shift_amount
      plain_text+=alphabet[new_position_after_shift]
    print(f"The decoded text is {plain_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if(direction=='encode'):
  encrypt(plain_text=text, shift_amount=shift)
else:
  decrypt(cipher_text=text, shift_amount=shift)

 