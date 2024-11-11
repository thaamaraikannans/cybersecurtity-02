str1=input("Enter the input :")
print(list(str1))
# str2=str1[::-1]
str2 = []
for char in str1:
    str2.insert(0, char)
# str2 = "".join(str2)
is_palindrome = True
print(str2)
for res in range(len(str1)):
    print(res)
    print("value checking is ", str1[res], str2[res])
    if str1[res] == str2[res]:
        is_palindrome = True
    else:
        is_palindrome = False
        break


if is_palindrome:
    print("pallindrome")
else:
    print("Not a pallindrome")