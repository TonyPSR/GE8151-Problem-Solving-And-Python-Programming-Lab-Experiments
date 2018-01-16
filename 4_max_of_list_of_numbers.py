#initializing variables
max = 0
numList = list() #declaring values as list

n = int(input('Enter the number of elements to find the maximum number:'))

for i in range(0, n): #loop for getting elements
    temp = int(input('Enter Element:'))
    numList.append(temp)


for x in range(0, n): #checking if elements are greater than previous max element
    if numList[x] > max:  #if yes, store that element in max and continue iteration
        max = numList[x]
    else:                # if no, go to the next iteration
        continue

print 'The greatest number in the list is -->',max