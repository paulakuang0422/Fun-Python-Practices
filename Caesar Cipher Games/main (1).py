alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#define the caesar funtion
def caesar(plain_text, shift_amount,cip_direction):
  final_text = ""
  if cip_direction == "decode":
    shift_amount*=-1
  for char in plain_text:
    if char in alphabet:
      position = alphabet.index(char)+shift_amount
      final_text += alphabet[position]
    else:
      final_text += char
  print(f"The {cip_direction} text is {final_text}")

#continue or not
game_over=False
from art import logo
print(logo)

while not game_over:
  #input all the variable, shift under modulus to get within 0-25
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(int(input("Type the shift number:\n"))%26)
  
  #excute caesar function
  caesar(plain_text=text,shift_amount=shift,cip_direction=direction.lower())
  check = input("Do you want to continue the game? type yes or no\n")
  if check == "no":
    game_over=True
    print("Bye Bye!欢迎下次再来！")
  
