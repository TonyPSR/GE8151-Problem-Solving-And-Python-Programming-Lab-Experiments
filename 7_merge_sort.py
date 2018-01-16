def mergeSort(list):
    if len(list) >= 2:
        midPoint = len(list) // 2
        leftHalf = list[:midPoint]
        rightHalf = list[midPoint:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        leftPointer = 0
        rightPointer = 0
        mainPointer = 0

        while leftPointer < len(leftHalf) and rightPointer < len(rightHalf):
            if rightHalf[rightPointer] < leftHalf[leftPointer]:
                list[mainPointer] = rightHalf[rightPointer]
                rightPointer += 1
                mainPointer += 1
            else:
                list[mainPointer] = leftHalf[leftPointer]
                leftPointer += 1
                mainPointer += 1

        while leftPointer < len(leftHalf):
            list[mainPointer] = leftHalf[leftPointer]
            leftPointer += 1
            mainPointer += 1

        while rightPointer < len(rightHalf):
            list[mainPointer] = rightHalf[rightPointer]
            rightPointer += 1
            mainPointer += 1

list = list()
n = int(raw_input('Enter the no. of elements:'))

#get the list of number:
for i in range(0,n):
    temp = int(raw_input('Enter Element:'))
    list.append(temp)

mergeSort(list)
print('\nThe sorted list:')
print(list)