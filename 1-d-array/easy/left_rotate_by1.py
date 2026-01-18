'''
Given an integer array nums, rotate the array to the left by one.
Note: There is no need to return anything, just modify the given array.
'''
class Solution:
    def rotateArrayByOne(self, nums):
        # print(id(nums))
        if len(nums) <= 1:
            return nums
        else:

            temp = nums[0]

            for i in range(1,len(nums)):
                nums[i-1] = nums[i]

            nums[i] = temp

            # print(id(nums))

            # print("rotated 1 place", rotated)

            return nums
        
# Example usage:
case1 = [1,2,3,4,5]
case2 = [10]
case3 = [7,8,9]
sol = Solution()
res1 = sol.rotateArrayByOne(case1)
print("Array after left rotation by 1 for case1:", res1)  # Output: [2, 3, 4, 5, 1]
res2 = sol.rotateArrayByOne(case2)
print("Array after left rotation by 1 for case2:", res2)  # Output: [10]
res3 = sol.rotateArrayByOne(case3)
print("Array after left rotation by 1 for case3:", res3)  # Output: [8, 9, 7]