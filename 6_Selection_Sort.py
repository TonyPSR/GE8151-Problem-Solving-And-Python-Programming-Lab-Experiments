def selectionSort(numList):
	#returns the list in a sorted manner.
	listLenght = len(numList)
	for i in range(0,listLenght):
		min_index = i
		for j in range(i+1,listLenght):
			if numList[min_index] > numList[j]:
				min_index = j
		#swaping element with index min_index with i
		numList[i], numList[min_index] = numList[min_index], numList[i]


numList = []
n = int(raw_input('Enter the no. of elements:'))

#get the list of number:
for i in range(0,n):
	temp = int(raw_input('Enter Element:'))
	numList.append(temp)

selectionSort(numList)
print '\nThe sorted list:'
print(numList)