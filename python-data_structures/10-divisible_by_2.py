#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []
    if my_list:
        for k in my_list:
            if k == 0:
                list_result.append('zero')
                continue
            if k % 2 == 0:
                list_result.append(k)
            else:
                list_result.append(None)
    return list_result
