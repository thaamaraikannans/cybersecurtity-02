# exception handling -> four blocks -> try, except, else and finally
try:
    def addition(num1, num2):
        try:
            return num1/num2
        except IndexError:
            print("Type error")
            return int(num1)/int(num2)
        except TypeError:
            print("Type error")
            return int(num1)/int(num2)
except NameError:
    print("Declare name properly")

# try:
#     print(addition(80, 70))
#     print(addition(90, "50"))
# except TypeError:
#     print("check your arguments")

# print("The code has been executed successfully")