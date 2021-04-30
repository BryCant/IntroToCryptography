# import my cipher methods
from wk1 import CipherMethods as cm

# 1
# a) Prompts the user to choose whether to encrypt or decrypt a message and loops if the user does not type valid choice
e_or_d = input("Would you like to Encrypt (E) or Decrypt (D)?  ")
while (e_or_d.lower() != 'e') and (e_or_d.lower() != 'd'):
    print("INVALID! Please enter 'E' for Encrypt OR 'D' for Decrypt.")
    e_or_d = input("Would you like to Encrypt (E) or Decrypt (D)? ")

# b) prompts the user for a cipher method (additive Caesar, one-time pad, Vigenere, or Substitution);
cipher_choice = input("Which cipher (additive Caesar [C], one-time pad [O], Vigenere [V], or Substitution [S])? ")
VALID_CIPHERS = ('c', 'o', 'v', 's')
while cipher_choice.lower() not in VALID_CIPHERS:
    print("INVALID! Please enter additive Caesar [C], one-time pad [O], Vigenere [V], or Substitution [S].")
    cipher_choice = input("Which cipher (additive Caesar [C], one-time pad [O], Vigenere [V], or Substitution [S])? ")

# c) prompts the user for an appropriate key depending on chosen method, and checks the key for errors;
if cipher_choice.lower() == 'c':
    cm.caesar(e_or_d)
elif cipher_choice.lower() == 'o':
    cm.otp(e_or_d)
elif cipher_choice.lower() == 'v':
    cm.vigenere(e_or_d)
elif cipher_choice.lower() == 's':
    cm.subst(e_or_d)
else:
    exit()

# 2) FTQ QZQYK UE AHQD FTQ YAGZFMUZ = THE ENEMY IS OVER THE MOUNTAIN
#    I STARTED FROM 26 THINKING IT WOULD BE FASTER!!!!!!!!!!!

# 3) AZGKM MIT EAM OL OF MIT QOMEITF TAMOFU MIT HONNA = ABORT THE CAT IS IN THE KITCHEN EATING THE PIZZA
#    don't even ask me about this one ... the is repeated 3 times ... A goes in between E and T ... rest of word eating
#    ... o is i, f is n, u is g ... the only two letter i word left 'is', ...

"""
4) Write a short essay detailing the weaknesses of the four encryption schemes in this project.

The Caesar Cipher is highly susceptible to brute force. Although it creates the illusion of gibberish, the cipher's 
method of encryption does not place the encrypted that far from the original message. To be more specific, there are
only 25 other doors (MAX) to knock on before finding your target. If someone is eager to decrypt this message, they
need only try every possible shift and determine (with our lovely pattern seeking brains) which permutation makes the 
most sense. Additive Caesar shift are easy but are not that strong.

The One Time Pad has its pros but the one stands out - it's unbreakable. The simple nature of this encryption is that 
the final message is the sum of the original message and the characters of a one time pad key. However, this complexity 
increases when examining the endless amount of ways to reach the same sum. Though this seems like the perfect cipher, 
this cryptic invincibility can only be attained after the one time pad key has been successfully delivered - without 
any middle men. This is where the cipher's weakness shines. The plain key must be delivered and - if intercepted - the 
encryption will unravel. Even to encrypt the key would lead to this conundrum once more. This makes the One Time Pad
very weak in a practical sense. Aside from this flaw, one would need multiple messages encrypted with the same one time
pad key to decipher the message.

The Vigenere cipher, One Time Pad's close cousin, shares a lot of these pros and cons. The cipher is close to unbreakable. 
The key poses the threat of easy interception. However a con dissonant from the One Time Pad is that the keys footprint 
can repeat within the bounds of one message. If a key repeats an adequate throughout the message, the periodicity of the 
encryption may be exposed. Consequently, the length of the key will be determined and the encryption is destined to 
unravel. This factors weaken the cipher, with its self-inflicted predisposition to vulnerability. (that last sentence 
was just for fun)

The Substitution cipher repeats some of the same arcs of the aforementioned ciphers. However the big flaw that it 
repeats is its susceptibility to brute force. Depending on the language, letters in words and sentences have a 
statistical frequency in there appearance. For example, vowels are used a lot in the english language because almost 
every word needs them. Therefore, letters can be determined after deep observation of patterns (such as three letter 
words most likely being 'the' or 'and'; one letter words being 'I' or 'a'; and so on). From these observation one would
build the encryption dictionary from which the message can be decrypted. 
"""
