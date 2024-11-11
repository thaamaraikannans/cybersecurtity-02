user_age = input("enter user age: ")
is_having_voter_id = input("is he/she has voter id ? (yes/no)")

if  (int(user_age) >= 18) and(is_having_voter_id == "yes"):
# if (not (int(user_age) < 18) ) and (not (is_having_voter_id == "no")):
    print("valid to vote")
elif is_having_voter_id == "no":
    print("you have to apply voter id and not possible to vote")
else:
    print("not possible to vote not meeting the age")
