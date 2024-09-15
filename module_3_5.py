def get_multiplied_digits(number):
    num=int(number)
    number=str(num)
    if len(number)>=1:
        if len(number)==1:
            return int(number[0])
        return int(number[0])*get_multiplied_digits(number[1:])
        

print(get_multiplied_digits("40203"))