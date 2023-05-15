# This approach remove 'in-place' duplicates in an array and gives back the number 
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


nums = [1, 1, 2]
print(removeDuplicates(nums))