import sys
from utils import user_input, debit_bal

def banking():
    number = user_input()
    if number:
        is_amount_debit = input("do you need to debit money ? yes/no :")
        if is_amount_debit == "yes":
            amount_debit = input("Enter Valid amount :")
            debit_bal(number, int(amount_debit))
            return
        else:
            print("Thank you banking")
            return

banking()
print(sys.version)