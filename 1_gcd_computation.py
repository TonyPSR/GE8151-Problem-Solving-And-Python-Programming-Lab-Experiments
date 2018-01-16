a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))

if a>b:
    #store the smaller number is a
    a,b = b,a

#special case where one of the either number is zero
#and the other is non-zero
if a == 0:
    print 'The GCD of',a,'and',b,'is',b
    exit()
if b == 0:
    print 'The GCD of',a,'and',b,'is',a
    exit()

#normal cases with two non-zeros or two zeros.
for i in range(a,0,-1): #loop: a,a-1,a-2,a-3,............1
    if (a%i == 0) and (b%i == 0):
        print 'The GCD of',a,'and',b,'is',i
        break