'''
Given an integer array nums, move all the 0's to the end of the array. 
The relative order of the other elements must remain the same.
This must be done in place, without making a copy of the array.
'''

class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        temp = [0] * n

        count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                temp[count] = nums[i]
                count += 1

        for i in range(count):
            nums[i] = temp[i]

        for i in range(count, len(nums)):
            nums[i] = 0

        return nums

# Example usage:
case1 = [0,1,0,3,12]
case2 = [0,0,1]
case3 = [4,2,4,0,0,3,0,5,1,0]
sol = Solution()
res1 = sol.moveZeroes(case1)
print("Array after moving zeros to end for case1:", res1)  # Output: [1, 3, 12, 0, 0]
res2 = sol.moveZeroes(case2)
print("Array after moving zeros to end for case2:", res2)  # Output: [1, 0, 0]
res3 = sol.moveZeroes(case3)
print("Array after moving zeros to end for case3:", res3)  # Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
