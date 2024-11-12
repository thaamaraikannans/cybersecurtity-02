def print_num(val1, val2):
    print("number 1 is",val1)
    print("number 2 is",val2)
    return 

# def addition(val1, val2, val3=True):
#     print("value 3 is", val3)
#     print_num(val1=val1, val2=val2)
#     response = val1+val2
#     print("The addition value is ", response)
#     init_value = 100
#     is_valid_adhaar = True
#     members = ["Kannan", "surya"]   
#     return members,response, init_value, is_valid_adhaar 


# def addition(*args):
#     print(*args)
#     val1=args[0] 
#     val2=args[1]
#     print_num(val1=args[0], val2=args[1])
#     response = val1+val2
#     print("The addition value is ", response)
#     init_value = 100
#     is_valid_adhaar = True
#     members = ["Kannan", "surya"]   
#     return members,response, init_value, is_valid_adhaar 

def addition(**kwargs):
    print(kwargs)
    val1=kwargs["val1"] 
    val2=kwargs["val2"]
    print_num(val1=kwargs["val1"], val2=kwargs["val2"])
    response = val1+val2
    print("The addition value is ", response)
    init_value = 100
    is_valid_adhaar = True
    members = ["Kannan", "surya"]   
    return members,response, init_value, is_valid_adhaar 

def subtraction(val1, val2):
    print_num(val1=val1, val2=val2)
    print("The subtraction value is", val1-val2)
    return

def multi(val1, val2):
    print_num(val1=val1, val2=val2)
    print("The multiplication value is ", val1*val2)
    return

def division(val1, val2):
    print_num(val1=val1, val2=val2)
    print("The division value is ", val1/val2)
    return

# addition(76,34)
addition_value = addition(val1=90, val2=100, brand="Realme")
addition_value2 = addition(val2=190, val1=693)

def dummy_func():
    pass


