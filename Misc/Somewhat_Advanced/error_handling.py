# Error (Exception) handlling

# type error
# syntax error
# name error
# index error
# key error
# Zero division error

while True:
    try:
        age = int(input("what is your age? "))
        # age / 0
        print(age)
        raise Exception("alaye cut it out mehn")
    except ZeroDivisionError:
        print("please enter an age greater than zero")
    # except:
    #     print("please enter a number")
    else:
        print("thank you")
        break
    finally:
        print("ok i am finally done")


# more error handling

def sum(num1, num2):
    try:
        return num1 + num2

    except (TypeError, ZeroDivisionError) as err:
        print(f"please enter numbers:- {err} " )


print(sum(1, '2'))
