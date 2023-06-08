#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    check_div = 0
    result = []
    for i in range(list_length):
        try:
            check_div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            check_div = 0
        except ZeroDivisionError:
            print("division by 0")
            check_div = 0
        except IndexError:
            print("out of range")
            check_div = 0
        finally:
            result.append(check_div)
    return result
