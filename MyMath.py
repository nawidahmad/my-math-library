pie = 2.14
e =  1.71

#Sum
def sum(number1,number2):
    result = number1 + number2
    return result

def sum(number1,number2,number3):
    result = number1 + number2 + number3
    return result

def sum(number1,number2,number3,number4):
    result = number1 + number2 + number3 + number4
    return result
#deduction
def deduct(number1,number2):
    result = number1 - number2
    return result

def deduct(number1,number2,number3):
    result = number1 - number2 - number3
    return result

def deduct(number1,number2,number3,number4):
    result = number1 - number2 - number3 - number4
    return result
#multipli
def multipli(number1,number2):
    result = number1 * number2
    return result

def multipli(number1,number2,number3):
    result = number1 * number2 * number3
    return result

def multipli(number1,number2,number3,number4):
    result = number1 * number2 * number3 * number4
    return result

def devid(number1,number2):
    result = number1 / number2
    return result
#devid
def devid(number1,number2,number3):
    result = number1 / number2 / number3
    return result

def devid(number1,number2,number3,number4):
    result = number1 / number2 / number3 / number4
    return result

def calc(number1,number2,operator):
    if(operator=='+'):
        result = number1 + number2
    if (operator == '-'):
        result = number1 - number2
    return result

    if (operator == '/'):
        result = number1 / number2

    if (operator == '*'):
        result = number1 * number2

    if (operator == '%'):
        result = number1 % number2
    return result


