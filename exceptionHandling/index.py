
def dummy_func(num1):
    try:
        response = num1/0.5
    except Exception as kanna:
        print(kanna)
    else:
        print(response)
    finally:
        print("Program call ----->>>>>>>>","i will run on all execution")
    return

try:
    dummy_func(10)
    dummy_func("10", "90")
except Exception as err:
    print("outer ---->>>>>",err)