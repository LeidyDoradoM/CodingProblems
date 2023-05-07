# remove duplicates from an array in-place.

from tokenize import StringPrefix


def removeDuplicates(nums):
    for i in range(len(nums)-1):
        value = nums[i]
        for j in range(i+1,len(nums)):
            if value == nums[j]:
                continue
            else:
                nums[i+1] = nums[j]
                k = i+2
                for k1 in range(j+1,len(nums)):
                    nums[k] = nums[k1]
                    k = k+1
                break 
    count = 0
    n=0
    while n < len(nums)-1:
        if nums[n]< nums[n+1]:
            count = count+1
        else:
            break
        n = n+1
    return (count+1,nums)


#nums = [0,0,0,0,0,1,1,2,2,3,3,4]

#(k, nums1) = removeDuplicates(nums)
#print(nums1)
#print(k)

# search the index of a target
def searchInsert(nums, target):
    start = 0
    end = len(nums)-1
    while end-start > 1:
        middle = (start+end)//2
        if nums[middle] < target:
            start = middle + 1
        else:
            end = middle -1

    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    if nums[start] < target and nums[end] > target:
        return end
    if nums[start] > target:
        return start
    if nums[end] < target:
        return end+1

nums = [1,3]
target =4
#print(searchInsert(nums,target))

def longestSubstring(string):
    if string == "":
        return 0
    elif len(string) == 1:
        return 1
    elif len(string) == 2:
        if string[0] != string[1]:
            return 2
        else:
            return 1
    else:
        i = 0
        j = 1
        count = 0
        longest = count
        while i < len(string):
            print('i:', i)
            while j < len(string):
                print('j:', j)
                if string[i] != string[j]:
                    j = j+1
                else:
                    i = j
                    count = i
                    j = i+1
                    print(count)
            
            if j == len(string):
                i = i+1
                count = i
                j = i+1
            if longest <= count:
                longest = count
                
        return longest

stri = 'aab'
#print(longestSubstring(stri))

# Median of 2 sorted arrays
def median2arrays(nums1,nums2):
    n = len(nums1)
    m = len(nums2)
    outarray = [None]*(n+m)
    i = 0
    j = 0
    while i < n and j < m:
        if nums1[i] < nums2[j]:
            outarray[i+j] = nums1[i]
            i = i+1
        else:
            outarray[i+j] = nums2[j]
            j = j+1

    if i == n:
        outarray[i+j:] = nums2[j:]
    if j == m:
        outarray[i+j:] = nums1[i:]
    print(outarray)
    if len(outarray)%2 == 0:
        median = (outarray[len(outarray)//2 - 1] + outarray[len(outarray)//2])/2
    else:
        median = outarray[len(outarray)//2]

    return median

nums1 = [1,2]
nums2 = [3,4]
#print(median2arrays(nums1,nums2))

# reverse integer
def reverse(x):
    flag = False
    if x < 0:
        x = abs(x)
        flag = True
    
    if x//10 == 0:
        if flag == True:
            return -x
        else:
            return x
    else:
        reversed = ''
        while x//10 != 0:
            residue = x%10
            cociente = x//10
            reversed = reversed+str(residue)
            x = cociente
        reversed= reversed+str(cociente)
        if flag == True:
            return -int(reversed)
        else:
            return int(reversed)
        

print(reverse(903))
