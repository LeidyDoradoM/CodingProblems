# This approach remove 'in-place' duplicates in a sorted array and gives back the number 
# of unique elements in the array, but this solutions isn't efficient when the array 
# is big and have a big number of repeated items.

def removeDuplicates(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  for i in range(len(nums) - 1):
    value = nums[i]
    for j in range(i + 1, len(nums)):
      if value == nums[j]:
        continue
      else:
        nums[i + 1] = nums[j]
        k = i + 2
        for k1 in range(j + 1, len(nums)):
          nums[k] = nums[k1]
          k = k + 1
        break
  count = 0
  n = 0
  while n < len(nums) - 1:
    if nums[n] < nums[n + 1]:
      count = count + 1
    else:
      break
    n = n + 1
  return [nums, count + 1]

def removeDuplicatesImproved(arr):
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

nums = [1,1,2]
print(removeDuplicatesImproved(nums))