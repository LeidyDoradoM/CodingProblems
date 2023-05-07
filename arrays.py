# practicing arrays functions for 2-d arrays
#import numpy as np

arr = [[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9],[0,1,2,3]] #numpy module can be used when creating 2D Arrays
print(arr)

# Accesing an element in a 2d array
def accesElement(arr,rowidx,colidx):
    if rowidx >= len(arr) or colidx >= len(arr[0]):
        print('Incorrect index')
    else:
        print(arr[rowidx][colidx])  
    return

#accesElement(arr,1,2)

# Traversing a 2d array
def traversingArrays(arr):
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            print(arr[row][col]) 
    return

#traversingArrays(arr)

# Seaching for an element in a 2d array
def searchElement(arr,value):
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if value == arr[row][col]:
                return (print('The value is at index: ', row,col))
   
    return (print('The value is not found'))

#searchElement(arr,20)

#print(np.delete(arr,1,axis=0))

 
