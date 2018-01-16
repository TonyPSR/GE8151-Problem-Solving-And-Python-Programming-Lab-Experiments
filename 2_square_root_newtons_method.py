#method 1:
def square_root(number):
    estimate = float(number/2)
    while True:
        newestimate = float(abs(((estimate + (number/estimate))/2)))
        if newestimate == estimate:
            return newestimate
        estimate = newestimate

num = int(input('Enter the number:'))
print square_root(num),'is the square root of',num

#method 2:
# def improve_guess(guess, num):
#     return float((guess + (num / guess)) / 2.0)
#
# def good_enough(guess, num):
#     d = abs(guess * guess - num) #guess squared ~= num
#     tolerance = 0.0000001 #floating point accuracy, can be changed.
#     return (d < tolerance)
#
# def start_guess(guess, num):
#     while(not good_enough(guess, num)):
#         guess = improve_guess(guess, num)
#     return guess
#
# def square_root(num):
#     r = start_guess(1, num)
#     return r
#
# num = int(input('Enter the number:'))
# print square_root(num),'is the square root of',num

