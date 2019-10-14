#Given an array nums, write a function to move all 0's to the end
#of it while maintaining the relative order of the non-zero elements.
def moveZeros(nums):
    index = 0
    for i in nums:
        if nums[index] == 0:
            nums.insert(len(nums),nums.pop(index))
        index += 1

    print(nums)

myList = [0,1,0,2,0,3,0,3,0,2,0,1,0]
print(moveZeros(myList))
