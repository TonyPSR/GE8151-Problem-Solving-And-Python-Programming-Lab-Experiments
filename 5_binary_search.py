#List must be sorted
#ascending order.
def binarySearch(numList, toFind):
    #returns the index of the toFind element in the list.
    #if not in the list returns False
    startPoint = 0
    endPoint = len(numList)

    for i in range(0, len(numList)):

        if toFind > numList[average(startPoint, endPoint)]:
            startPoint = average(startPoint,endPoint)

        elif toFind < numList[average(startPoint, endPoint)]:
            endPoint = average(startPoint,endPoint)

        elif toFind == numList[average(startPoint, endPoint)]:
            return (average(startPoint,endPoint))

    return False

def average(num1,num2):
    #returns average of num1 and num2 as integer
    return (num1+num2)//2

numList = list()
n = int(raw_input('Enter the no. of elements:'))
print('Enter the elements in sorted order.')
#get the list of number:
for i in range(0,n):
    temp = int(raw_input('Enter Element'))
    numList.append(temp)


toFind = int(raw_input('Enter the element to find:'))

#print the index of number to find the list if the element's in the list.
#index starting from 0.
result = binarySearch(numList, toFind)
if result == False:
    print 'The element is not found in the list.'
else:
    print 'The position of',toFind,'in the list is:',result