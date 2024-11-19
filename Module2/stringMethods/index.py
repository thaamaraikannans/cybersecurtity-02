import string
# name = "Hello!,Hi!,Welcome!,ThankYou!"
password = "KANNANv123"
# print(name.split(","))
lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
numbers = list(string.digits)

is_upper = False
is_lower = False
is_number = False

for lower in lower_case:
    val = password.count(lower)
    if val > 0:
        is_lower = True

for upper in upper_case:
    if upper in password:
        is_upper = True

for digit in numbers:
    if digit in password:
        is_number = True
        

if is_number and is_lower and is_upper:
    print("valid password")
else:
    print("Invalid password")