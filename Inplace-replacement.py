# 1. remove duplicates from a sorted array (in-place), this solution could be also found in 
# remduplicatesinArray.py
def removeDuplicates(arr):
    n = len(arr)
    if n == 0:
        return 0
    indx = 0
    prev = arr[0]
    for i in range(0,n):
        if arr[i] != prev:
            arr[indx+1] = arr[i]  
            indx = indx+1
            prev = arr[i]
    return indx+1
#-------------------------------------
#2. Given a sorted array of integers and a target, find the index of the target if it is in the
# array. If not, the index where it would be if it were inserted in order
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
# --------------------------------------
# 3. find the longest substring 
def longestSubstring(s):
    if s == "":
        return 0
    else:
        letters = {}
        count = 0 
        long = []
        for idx in range(len(s)):
            flag = 0
            print('Idx',idx)
            for i in s[idx:]:
                print('string:', s[idx:])
                if i not in letters:
                    letters[i]= 1
                    count = count+1
                    print('not i',i)
                    print('not i',count)
                else:
                    flag = 1
                    print('i',i)
                    long.append(len(letters))
                    print('long string:',long)
                    break
            if flag == 0:
                long.append(count)
            letters = {}
            count = 0
        print(long)
        longest = max(long)              
        return longest 
stri = 'abcbbcc'
print(longestSubstring(stri))
#----------------------------------
# 4. Given two sorted arrays, return the median of the two sorted arrays in O(log(m+n)) time
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
    #print(outarray)
    if len(outarray)%2 == 0:
        median = (outarray[len(outarray)//2 - 1] + outarray[len(outarray)//2])/2
    else:
        median = outarray[len(outarray)//2]

    return median

#nums1 = [1,2]
#nums2 = [3,4]
#print(median2arrays(nums1,nums2))
#-------------------------------------
# 5. given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
# the value to go outside the signed 32-bit integer range [-2^31,2^31 -1], then return 0.
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
        if int(reversed) >=2**31-1 or int(reversed) <=-2**31: return 0
        else:
            if flag == True:
                return -int(reversed)
            else:
                return int(reversed)      
#print(reverse(903))
