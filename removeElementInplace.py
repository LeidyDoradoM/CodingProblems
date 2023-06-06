# Remove Element: given an array, nums, and an integer, val, remove all occurrences of val in nums in-place
# The orde of the elements may be changed. Then return the number of elements in nums which
# are not equal to val.

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count = 0
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == val:
            temp = nums[i]
            nums[i] = nums[i+1]

            count = count+1
            print('count', count)
        else:
            i = i+1
            print(i)
    if nums[i] == val:
        count = count+1
        nums[i] = 0

    print('array:', nums)
    return n-count

arr = [0,1,2,2,3,0,4,2]
value = 2
print(removeElement(arr,value))