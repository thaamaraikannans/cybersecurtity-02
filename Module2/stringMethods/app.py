# string in python, its a collection characters
# (alphabetical, numerical, operators, special characters and symbols)

# " "  or ' ' or """ """

value_sub = "English, tamil , Maths, science, Social"
print(value_sub)
# lower level repetative and general need functions 
# were available in python is methods 
# -> string methods
# -> list methods
# -> dict methods

lower_sub = value_sub.casefold()
print(lower_sub)
# capital_sub = lower_sub.capitalize()
# print(capital_sub)
# print(value_sub.capitalize())
list_sub = lower_sub.split(",")
capital_sub = []
for sub in list_sub:
    print(sub)
    sub_cap = sub.strip().capitalize()
    capital_sub.append(sub_cap)
    print(capital_sub)
capital_sub = ", ".join(capital_sub)
print(capital_sub)