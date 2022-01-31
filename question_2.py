def is_leapyear(x):
    if (x % 400 == 0) and (x % 100 == 0):
        return True
    elif (x % 4 == 0) and (x % 100 != 0):
        return True
    else:
        return False
        
print(is_leapyear(1996))