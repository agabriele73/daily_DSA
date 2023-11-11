from array import *



# 1. Create an array and traverse.
print("\nCreate an array and traverse: ")
my_array = array('i', [1, 2, 3, 4, 5, 6, 7, 8])

print("Original Array: ", my_array)
for i in range(len(my_array)):
    print(f"Element at index {i}: {my_array[i]}")

# 2. Access individual elements through indexes
print("\nAccessing Elements Through Indexes: ")
element_at_index_0 = my_array[0]
element_at_index_1 = my_array[1]

print(f"element at 0: {element_at_index_0}")
print(f"element at 1: {element_at_index_1}")

# 3. Append any value to the array using append() method
print("\nAppend value to array: ")
print("Original Array: ", my_array)
my_array.append(9)
print("Array after appending: ", my_array)

# 4. Insert value in array using insert() method
print("\nInsert Value Into Array: ")
print("Original Array: ", my_array)
my_array.insert(2, -1)
print("Array After Inserting: ", my_array)

# 5. Extend python array using enxtend() method
print("\nExtend Python Array Using extend(): ")
new_arr = array('i', [10, 11, 12])
print("New List: ", new_arr)
my_array.extend(new_arr)
print("Array after extending: ", my_array)

# 6. Add items from list into array using fromList() method
print("\nAdd Items From List To Array Using fromlist(): ")
tempList = [20, 21, 22]
print("Original array", my_array)
my_array.fromlist(tempList)
print("Updated Array: ", my_array)

# 7. Remove any array element using remove() method
print("\nRemove Element From Array: ")
print("Original Array: ", my_array)
my_array.remove(-1)
print("Array after removing: ", my_array)

# 8. Remove any last array element using pop() method
print("\nRemove Last Element From Array: ")
print("Original Array: ", my_array)
last_elem = my_array.pop()
print(f"Last Element Removed: {last_elem}")
print("Array after popping: ", my_array)

# 9. Fetch any element through its index using index() method
print("\nFetch Any Element Through Its Index Using index(): ")
print(f"Element 6 at index: {my_array.index(6)}")

# 10. Reverse a python array using reverse() method
print("\nReverse A Python Array Using reverse(): ")
print("Original Array: ", my_array)
my_array.reverse()
print("Reversed Array: ", my_array)

# 11. Get array buffer information through buffer_info() method
print("\nGet Array Buffer Information Through buffer_info(): ")
bufferInfo = my_array.buffer_info()
print(bufferInfo)
# 12. Check for number of occurrences of an element using count() method
print("\nCheck For Number Of Occurrences Of An Element Using count(): ")
print(f"Number of times -1 occurs in the array: {my_array.count(-1)}")

# 13. Convert array to string usin tobytes() method
print("\nConvert Array To String Using toString(): ")
tempStr = my_array.tobytes()
print(tempStr)
# 15. Append a string to char array using fromstring() method
ints = array('i')
ints.frombytes(tempStr)
print("\nConverting back to ints: ", ints)

# 14. Convert array to a python list with the same elements using tolist() method
print("\nConvert to list:")
tempList = my_array.tolist()
print(tempList)
# 16. Slice elements from an array
print("\nSlicing elements:")

print("first 3",my_array[0:3])

print("last element",my_array[-1:])


# TWO DIMENSIONAL ARRAYS

# day 1 - 11, 15, 10, 6
# day 2 - 10, 14, 11, 5
# day 3 - 12, 17, 12, 8
# day 4 - 15, 18, 14, 9

import numpy as np

twoDarray = np.array([  [11, 15, 10, 6],
                        [ 10, 14, 11, 5],
                        [12, 17, 12, 8],
                        [15, 18, 14, 9]  
                        ])

print("\nTwo Dimensional Array: \n", twoDarray)
# insert new column axis = 1 insert new row axi = 0, same for append
# but only axis needed

newTwoDArray = np.insert(twoDarray, 0, [[1,2,3,4]], axis=0)
print("\nNew Two Dimensional Array after inserting: \n", newTwoDArray)

newTwoDArray = np.append(twoDarray, [[1,2,3,4]], axis=0)
print("\nNew Two Dimensional Array after appending: \n", newTwoDArray)


print("\nthis is element at row 2 column 3:",twoDarray[2][3])

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("Incorrect index")
    else:
        print(array[rowIndex][colIndex])

print("\nDifferent way")
accessElements(twoDarray, 2, 3)

print("\ntraversing a 2D array:")

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(twoDarray[i][j])

traverseTDArray(twoDarray)

print("\bLinear Search 2D:")
def linearSearchTD(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return f"value is located st index "+"row " +str(i)+" column "+str(j)
    return "element not found"

print(linearSearchTD(twoDarray, 17))


print("\nDelete column or row from 2D array: \n")
print(twoDarray)
newTDArray = np.delete(twoDarray, 0, axis=0)
print("\nafter delete:\n",newTDArray)