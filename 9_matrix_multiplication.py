
def getMatrix(matrix):
    row = int(input('Enter the no. rows:'))
    column = int(input('Enter the no. columns:'))
    tempList = list()
    temp = 0
    for i in range(row):
        for j in range(column):
            temp = int(raw_input('Enter element [{0}][{1}]'.format(i,j)))

            tempList.append(temp)
        matrix.append(tempList)
        tempList = []

def multiplyMatrix(matrix1,matrix2):
    resultMatrix = list()
    tempList = [];temp =0
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            tempList.append(0)
        resultMatrix.append(tempList)
        tempList = []
    if len(matrix1[0]) == len(matrix2):
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    resultMatrix[i][j] = resultMatrix[i][j] + (matrix1[i][k]*matrix2[k][j])
        print('\nResultant Matrix:')
        for i in range(len(resultMatrix)):
            print(resultMatrix[i])
    else:
        print 'invalid operation.'

matrix1 = list()
matrix2 = list()

print 'Matrix A: \n'
getMatrix(matrix1)

print 'Matrix B: \n'
getMatrix(matrix2)

multiplyMatrix(matrix1,matrix2)



