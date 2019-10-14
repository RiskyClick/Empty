#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice
#in the array, and it should return false if every element is distinct.

def containsDuplicate(nums):
    nums.sort()
    index = 0
    while index < len(nums) - 1:
        if nums[index] == nums[index + 1]:
            return True
        index += 1
    return False
########Method 1###############
    left = 0
    right = len(nums) - 1
    while True:
        if right <= 0 or left == right:
            return False
        elif nums[left] == nums[right]:
            return True
        elif right - left == 1:
            left += 1
            right = len(nums) - 1
        else:
            right -= 1
##########Method 2##############
    
            
myList = [3,3]
print(containsDuplicate(myList))
