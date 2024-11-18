# check the condition to do

user_data = input("enter name : ")
list_of_users = []

while user_data != "-":
    list_of_users.append(user_data)
    user_data = input("enter name : ")

print(list_of_users)