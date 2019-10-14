#Given a sorted array nums, remove the duplicates in-place such that each
#element appear only once and return the new length.
#Do not allocate extra space for another array, you must do this by
#modifying the input array in-place with O(1) extra memory.
def removeDuplicates(nums):
    left = 0                                            #LeftHand side of the array
    right = len(nums) - 1                               #Righthand side of the array
    while True:
        if len(nums) <= 1 or len(nums) - left <= 1:     #if given array only has one int OR if the LeftHand has traversed the list
            break
        elif right - left == 1:                         #Resets the Righthand to the right and moves the Lefthand along by one
            if nums[left] == nums[right]:               #if the numbers are the same and are next to eachother
                nums.pop(right)                         #pop Righthand, reset righthand to the end of the list and move lefthand over by one
                left = left + 1
                right = len(nums) - 1
            else:                                       #if the left and right hand are next to eachother but Not the same int
                left = left + 1
                right = len(nums) -1  
        elif nums[left] == nums[right]:                 #if the righthand and lefthand are the same int
            nums.pop(right)                             #pop the righthand and move it one int closer to the lefthand
            right = right - 1
        else:                                           #if the right and left hand are NOT next to eachother AND not the same int move the righthand closer to the lefthand
            right = right - 1
            
    return len(nums)                                    #returns the size of the array with no douplicate ints

myArray = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]               #Enter your own values here
print(removeDuplicates(myArray))
