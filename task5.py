def check_values(a, b):
    if a is True and b is False:
        return True
    elif a is None and b is None:
        return None
    else:
        if a > b:
            return 1
        elif a < b:
            return -1
        elif a == b:
            return 0
   
flag = True
while flag == True:
    flag = False