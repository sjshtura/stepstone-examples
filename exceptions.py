import math, sys

while True:
    try:
        x = int(input("Please enter a number: "))
        print(1/x)
        print(x[0])
        break
    # except ValueError as err:
    #     print("error message: ", err)
    #     print("No valid number. Try again!")
    # except ZeroDivisionError:
    #     print('Cannot divide by zero!')
    # except SystemExit:
    #     print('goodbye!')
    #     sys.exit()
    # except:
    #     print('Something else went wrong!')
    #     raise
    except:
        pass