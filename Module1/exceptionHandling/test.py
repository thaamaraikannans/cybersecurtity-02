# import app

try:
    def dummy_func(num1):
        response = num1/0.5
        print(response)
        return
    dummy_func(10)
    from app import addition
    print(addition(10, 20))
except Exception as err:
    print("outer ---->>>>>",err)