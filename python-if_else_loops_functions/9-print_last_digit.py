def print_last_digit(number):
    if number < 0:
        last =  number *-1
        last = last % 10
        print("{}".format(last), end="")
        return last
    last = number % 10
    print("{}".format(last), end="")
    return last
