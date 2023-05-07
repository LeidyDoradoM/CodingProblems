# Exercises for practicing list & array - no examples but exam
# 
# 1. Middle function -> from a list returns a new list with all elements but the first and last element
def middle(lst):
    n = len(lst)
    newlst = lst[1:n-1]
    return newlst

lst = [1,2,3,4]
#print(middle(lst)) 

# 2. 2D lists -> given 2d list calculate the sum of diagonal elements
def sumDiagonal(a):
    sum = 0
    for i in range(len(a)):
        sum = a[i][i] + sum
    
    return sum

mylist2d = [[1,2,3],[4,5,6],[7,8,9]]
#print(sumDiagonal(mylist2d))

# 3. Best Score -> given a list, write a function to get first and second best scores from the list (may contain duplicates)
def firstSecond(mylist):
    mylist.sort()
    return (mylist[-1],mylist[-2])

lst = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(firstSecond(lst))

# 4. Missing number -> find the missing number in a given integer array of 1 to n
def missingNumber(lst,n):
    totalsum = n*(n+1)/2
    cumsum = 0
    for item in lst:
        cumsum = item+cumsum
    return (totalsum-cumsum)

# 5. Duplicate Number -> write a function to find the duplicate number on a given integer array/list
def removeDuplicates(arr):
    newarray = list(range(len(arr)))
    for i in range(len(arr)):
        count = 0
        for j in range(i+1,len(arr)): 
            if arr[i] == arr[j]:
                count += 1
        newarray[i] = count
    output = []
    for i in range(len(newarray)):
        if newarray[i] == 0:
            output.append(arr[i])
    return output

print(removeDuplicates([1,1,2,2,3,4,5]))

# 6. Pairs -> write a function to find all pairs of an integer array whose sum is equal to a given number
def pairSum(myList,sum):
    output = []
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i]+myList[j]==sum:
                output.append(str(myList[i])+'+'+str(myList[j]))
    return output

print(pairSum([2,4,3,5,6,-2,4,7,8,9],7))