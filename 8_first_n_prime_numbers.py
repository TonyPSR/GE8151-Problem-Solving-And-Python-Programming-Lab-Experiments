n = int(raw_input('Enter the value of n:'))

for number in range(2,n+1):
    flag = False
    for factor in range(2,number):
        if number%factor == 0:
            flag = True

    if flag == False:
        print(number)