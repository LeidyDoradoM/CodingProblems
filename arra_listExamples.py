# Common interview problems

#1. Missing Number -> how to find a missing number in a list from 1 to n

n = 20
mylist = [1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20]

def findMissingN(mylist,n):
    sum1  = n*(n+1)/2
    sum2 = sum(mylist)
    print(sum1-sum2)

findMissingN(mylist,n)

#2. Two Sum -> given an array of integers (nums) and an integer (target), return indices of
# the two numbers such that they add up to target

nums = [2,7,11,15]
target = 9

def twoNumbers(nums,target):
    #output = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i]+nums[j] == target:
               # output.append(i)
               # output.append(j)
               print(i,j)
    return 

twoNumbers(nums,target)

# 3. How to find if a number exists in an array. Output: false or true 

import numpy as np

myarray = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])
number = 30

def findNumber(array,numb):
    for item in array:
        if item == numb:
            return True
    
    return False

print(findNumber(myarray,number))

# 4. How to find maximum product of two integers in an array, when all integers are positive

def findMaxProd(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j] > maxProduct:
                maxProduct = array[i]*array[j]
                pair = str(array[i])+','+str(array[j])
    return (maxProduct,pair)

print(findMaxProd(myarray))

# 5. Is Unique? Implement an algorithm to determine if a list has all unique characters, using python lists

mylist = [1,20,30,44,5,56,57,8,10,31,12,13,14,35,16,27,58,19,21]

def IsUnique(mylist):
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            if mylist[i] == mylist[j]:
                print(mylist[i])
                return False
                
    return True

print(IsUnique(mylist))

# 6. Permutation -> Given two lists, find if one is a permutaion of the other

def permuted(list1,list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

list1 = ['a','b','c']
list2 = ['c','c','a']
print(permuted(list1,list2))

# 7. Rotate a matrix - 