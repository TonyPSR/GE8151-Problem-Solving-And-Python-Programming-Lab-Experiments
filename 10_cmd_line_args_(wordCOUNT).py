#word count for single line from txt file.
import sys

path = sys.argv[1]


# with open(path,'r') as fptr:
#     lineContent = fptr.readline()
#
# wordContent = lineContent.split(' ')
# print(lineContent)
# print('The no of words in the files is {}'.format(len(wordContent)))


# #word count for multi line from txt file.
# import sys
#
# path = sys.argv[1]


totalWord = []
with open(path,'r') as fptr:
    #read the file, store muliple lines as list
    fileContent = fptr.readlines()

for line in fileContent:
    #remove \n escape sequence from list elements
    #and spilt each element with respect to ' '(space)
    #store in totalWord as list
    line = line.strip('\n')
    totalWord.extend(line.split(' '))
    print(line)


print('\n\nThe no of words in the file is {0}'.format(len(totalWord)))