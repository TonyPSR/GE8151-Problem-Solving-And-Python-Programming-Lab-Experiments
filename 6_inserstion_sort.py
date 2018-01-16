def insertionSort(numList):
    for i in range(1, len(numList)):
        holePosition = i
        elementConsidered = numList[i]
        while holePosition > 0 and elementConsidered < numList[holePosition-1]:
            numList[holePosition] = numList[holePosition - 1]
            holePosition -= 1
        numList[holePosition] = elementConsidered

numList = []
n = int(input('Enter the number of elements:'))
for i in range(0, n): #loop for getting elements
    temp = int(input('Enter Element:'))
    numList.append(temp)
print('\nThe sorted list:')
insertionSort(numList)
print(numList)