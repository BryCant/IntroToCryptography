import string
import math


# ------------ Caesar Cipher Method --------------- #
def caesar(e_or_d):
    # 1) Ask user for a plaintext or ciphertext message (all lowercase).
    message = input("Please enter your plaintext or ciphertext message (all lowercase): ")

    # 2) Ask user for additive encryption shift
    got_shift = False
    while not got_shift:
        try:
            shiftNum = int(input("What is the caesar shift magnitude? "))
            got_shift = True
        except ValueError:
            print("Please enter number!")
            got_shift = False

    # 3) Shift message
    shifted_message = ""
    if e_or_d.lower() == 'e':
        for letter in str(message).lower():
            shifted_message += chr(
                (((ord(letter) - 97) + shiftNum) % 26) + 97) if letter in string.ascii_lowercase else letter
    elif e_or_d.lower() == 'd':
        for letter in str(message).lower():
            shifted_message += chr(
                (((ord(letter) - 97) - shiftNum) % 26) + 97) if letter in string.ascii_lowercase else letter
    else:
        print('Invalid input!')
        exit()

    print(f"Shifted message: \n{shifted_message}")
# -------------------------------------------------- #


# ------------- OTP Method -------------- #
def otp(e_or_d):
    # (a) Prompts the user for a numerical message separated by spaces;
    has_numbers = True
    message = ""
    while has_numbers:
        bingo_list = []
        message = input("Please enter your message (letters only): ")
        for letter in message:
            try:
                if isinstance(int(letter), int):
                    bingo_list.append("bingo")
            except ValueError:
                continue
        has_numbers = False if "bingo" not in bingo_list else True

    # (b) prompts the user for a numerical one-time pad;
    otp_key = input("Please enter your one time pad key: ")
    while len(otp_key) < len(message):
        print(f"INVALID; OTP Needs at least {len(message)} characters")
        otp_key = input("Please enter your one time pad key: ")

    # (c) prints the encrypted message.
    new_message = ""
    for i in range(len(message)):
        if e_or_d.lower() == 'e':
            new_message += chr(((ord(message[i]) + ord(otp_key[i]) - 194) % 26) + 97) if message[i] != " " else " "
        elif e_or_d.lower() == 'd':
            new_message += chr(((ord(message[i]) - ord(otp_key[i])) % 26) + 97) if message[i] != " " else " "

    print(new_message)
# ----------------------------------------- #


# ------------- Vigenere Method -------------- #
def vigenere(e_or_d):
    # (a) Prompts the user for a numerical message separated by spaces;
    message = input("Please enter your message (letters only): ")

    # (b) prompts the user for a one-time pad;
    vig_key = input("Please enter your vigenere one time pad key: ")
    while len(vig_key) >= len(message):
        print(f"INVALID; Vigenere OTP Key should be at MAX {len(message) - 1} characters")
        vig_key = input("Please enter your vigenere one time pad key: ")

    # (c) prints the encrypted numerical message.
    new_message = ""
    for i in range(len(message)):
        if e_or_d.lower() == 'e':
            new_message += chr(((ord(message[i]) + ord(vig_key[i % len(vig_key)]) - 194) % 26) + 97) if message[
                                                                                                            i] != " " else " "
        elif e_or_d.lower() == 'd':
            new_message += chr(((ord(message[i]) - ord(vig_key[i % len(vig_key)])) % 26) + 97) if message[
                                                                                                      i] != " " else " "

    print(new_message)
# ----------------------------------------------- #


# ------------- Substitution Method -------------- #
def subst(e_or_d):
    # (a) Prompts the user to enter message
    message = input("Please enter your message: ")

    # (b) Asks user for dictionary
    dict_or_def = input("Do you have a dictionary (Y/N)? ")
    while (dict_or_def.lower() != 'y') and (dict_or_def.lower() != 'n'):
        print("Please enter Y or N!")
        dict_or_def = input("Do you have a dictionary (Y/N)? ")

    sub_dict = {}
    if dict_or_def.lower() == 'y':
        usr_dict = input("Please enter substitution alphabet without spaces: ")
        for l_i in range(len(string.ascii_lowercase)):
            if e_or_d.lower() == 'e':
                sub_dict[string.ascii_lowercase[l_i]] = usr_dict[l_i]
            elif e_or_d.lower() == 'd':
                sub_dict[usr_dict[l_i]] = string.ascii_lowercase[l_i]
    elif dict_or_def.lower() == 'n':
        print("Using default dictionary ...")
        if e_or_d.lower() == 'e':
            sub_dict = {'a': 'q', 'c': 'w', 'b': 'e', 'e': 'r', 'd': 't', 'g': 'y', 'f': 'u', 'i': 'i', 'h': 'o',
                        'k': 'p', 'j': 'a', 'm': 's', 'l': 'd', 'o': 'f', 'n': 'g', 'q': 'h', 'p': 'j', 's': 'k',
                        'r': 'l', 'u': 'z', 't': 'x', 'w': 'c', 'v': 'v', 'y': 'b', 'x': 'n', 'z': 'm'}
        elif e_or_d.lower() == 'd':
            sub_dict = {'q': 'a', 'w': 'c', 'e': 'b', 'r': 'e', 't': 'd', 'y': 'g', 'u': 'f', 'i': 'i', 'o': 'h',
                        'p': 'k', 'a': 'j', 's': 'm', 'd': 'l', 'f': 'o', 'g': 'n', 'h': 'q', 'j': 'p', 'k': 's',
                        'l': 'r', 'z': 'u', 'x': 't', 'c': 'w', 'v': 'v', 'b': 'y', 'n': 'x', 'm': 'z'}

    # (c) prints the encrypted message.
    new_message = ""
    for index in range(len(message)):
        new_message += sub_dict[message[index]]

    print(new_message)
# ------------------------------------------------- #
