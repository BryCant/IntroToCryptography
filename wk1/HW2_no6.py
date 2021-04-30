# (a) Prompts the user for a numerical message separated by spaces;
num_mess = input("Please enter your numerical message (separated by spaces): ")
num_mess_list = num_mess.split()

# (b) prompts the user for a numerical one-time pad;
otp = input("Please enter your one time pad (separated by spaces): ")
otp_list = otp.split()
while len(otp_list) != len(num_mess_list):
    print(f"INVALID; OTP Needs {len(num_mess_list)} objects")
    otp = input("Please enter your one time pad (separated by spaces): ")
    otp_list = otp.split()

# (c) prints the encrypted numerical message.
new_message = ""
for index in range(len(num_mess_list)):
    new_message += str(int(num_mess_list[index]) + int(otp_list[index])) + " "

print(new_message)
