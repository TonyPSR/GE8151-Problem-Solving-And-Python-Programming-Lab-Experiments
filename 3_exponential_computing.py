def exponent(base,exp):
    result = 1
    if exp == 0:
        return 1
    for i in range(0,exp):
        result = result * base
    return result

b = int(raw_input('Enter the Base Value:'))
e = int(raw_input('Enter the Exponent Value:'))


print b,'raise to',e,'is',exponent(b,e)