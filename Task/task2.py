
str1=input("Enter the input :")
print(list(str1))
str2 = []
for char in str1:
    str2.insert(0, char)
str2 = "".join(str2)

str1 = "".join(str1)
str2 = "".join(str2)

print(str1 + " and " + str2)
if(str2==str1):
    print("pallindrome")
else:
    print("Not a pallindrome")
