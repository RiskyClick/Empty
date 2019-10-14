#Given a non-empty array of integers, every element appears twice except
#for one. Find that single one.

def singleNumber(nums):
    nums.sort()
    index = 0
    while index < len(nums) - 1:
        if nums[index] != nums[index + 1]:
            return nums[index]
        index += 2
    return nums[index]
myList = [4,1,2,1,2]
print(singleNumber(myList))
