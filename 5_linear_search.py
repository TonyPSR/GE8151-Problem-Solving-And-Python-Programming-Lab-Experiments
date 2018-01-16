def linearSearch(numList, toFind):
    #returns the index of toFind in list
    for i in range(0, len(numList)):
        if numList[i] == toFind:
            return i
    return False

numList = list()
n = int(raw_input('Enter the no. of elements:'))

#get the list of number:
for i in range(0,n):
    temp = int(raw_input('Enter Element:'))
    numList.append(temp)

toFind = int(raw_input('Enter the element to find:'))

#print the index of number to find the list if the element's in the list.
#index starting from 0.
result = linearSearch(numList, toFind)
if result == False:
    print 'The element is not found in the list.'
else:
    print 'The position of',toFind,'in the list is:',result