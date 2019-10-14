#Given an array of integers, return indices of the
#two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution,
#and you may not use the same element twice.
def twoSum(nums, target):
    #METHOD 1 FAST
    d={}
    for i,num in enumerate(nums):
        if target-num in d:
            return d[target-num], i
        d[num]=i

    #METHOD 2 NOT SO FAST!
##    index = 0
##    inc = index + 1
##    two = []
##    while index < len(nums) - 1:
##        if nums[index] + nums[inc] == target:
##            two.append(index)
##            two.append(inc)
##            return two
##            print(two)
##            return two
##        if inc == len(nums) - 1:
##            index += 1
##            inc = index + 1
##        else:
##            inc += 1

mylist = [3,2,4]
target = 6
print(twoSum(mylist, target))
