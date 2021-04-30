import string


# 0) Ask user whether program should encrypt or decrypt
enOrDe = input("Would you like to Encode or Decode your message? (E or D) ")

# 1) Ask user for a plaintext or ciphertext message (all lowercase).
message = input("Please enter your plaintext or ciphertext message (all lowercase): ")

# 2) Ask user for additive encryption shift
shiftNum = int(input("What is the caesar shift magnitude? "))

# 3) Shift message
shifted_message = ""
if enOrDe.lower() == 'e':
    shift_dict = {i: string.ascii_lowercase[(i + shiftNum) % 26] for i in range(len(string.ascii_lowercase))}
    for letter in str(message).lower():
        shifted_message += shift_dict[string.ascii_letters.index(letter)] if letter in string.ascii_lowercase else letter
elif enOrDe.lower() == 'd':
    shift_dict = {i: string.ascii_lowercase[(i - shiftNum) % 26] for i in range(len(string.ascii_lowercase))}
    for letter in str(message).lower():
        shifted_message += shift_dict[string.ascii_letters.index(letter)] if letter in string.ascii_lowercase else letter
else:
    print('Invalid input!')
    exit()

# 4) print shifted message.
print(f"Shifted message: \n{shifted_message}")

# alt way of shifting using ord and chr
shifted_message = ""
if enOrDe.lower() == 'e':
    for letter in str(message).lower():
        shifted_message += chr((((ord(letter) - 97) + shiftNum) % 26) + 97) if letter in string.ascii_lowercase else letter
elif enOrDe.lower() == 'd':
    for letter in str(message).lower():
        shifted_message += chr((((ord(letter) - 97) - shiftNum) % 26) + 97) if letter in string.ascii_lowercase else letter
else:
    print('Invalid input!')
    exit()

print(f"Shifted message again: \n{shifted_message}")
