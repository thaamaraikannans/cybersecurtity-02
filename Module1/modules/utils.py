from user.variables import user_name

def check_bal(account_num):
    for value in user_name:
        if value["account_number"]== account_num:
            print("Name is ", value["name"])
            print("Account Number is ", value["account_number"])
            print("The Available Balancer is ", value["bank_details"]["aval_bal"])
            return True

def user_input():
    acc_num = int(input("enter account number:"))
    res = check_bal(account_num=acc_num)
    if res:
        return acc_num
    else:
        print("Invalid Account number")
        return None

def debit_bal(acc_num, val):
    for value in user_name:
        if value["account_number"]== acc_num:
            bal= value["bank_details"]["aval_bal"]
            if bal > val:
                avail_bal = bal-val
                value["bank_details"]["aval_bal"] = avail_bal
                print("Available Balance",value["bank_details"]["aval_bal"] )
            else:
                print("InSufficient Balance")
            return