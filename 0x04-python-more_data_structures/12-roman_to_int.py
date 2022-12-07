#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    num = 0
    res = 0
    aux = 0
    list_num = []

    for s in roman_string:
        if s == 'I':
            num = 1
        elif s == 'V':
            num = 5
        elif s == 'X':
            num = 10
        elif s == 'L':
            num = 50
        elif s == 'C':
            num = 100
        elif s == 'D':
            num = 500
        elif s == 'M':
            num = 1000
        list_num.append(num)

    len_list = len(list_num)
    if len_list > 1:
        for i in range(1, len_list):
            if list_num[i] > list_num[i - 1]:
                    aux = list_num[i] - list_num[i - 1]
                    list_num[i] = aux
                    list_num[i - 1] = 0
    for num in list_num:
        res += num
    return
