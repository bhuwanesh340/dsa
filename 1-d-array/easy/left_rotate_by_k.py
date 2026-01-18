'''
Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.
'''

class Solution:
    def rotateArray(self, nums, k: int) -> None:
        if len(nums) <= 1:
            return nums
        else:

            # for i in range(k):
            #     temp = nums[0]
            #     for j in range(1, len(nums)):
            #         nums[j-1] = nums[j]

            #     nums[j] = temp

            # return nums

            k = k%n
            temp = []

            for i in range(k):
                temp.append(nums[i])

            for i in range(k,len(nums)):
                nums[i-k] = nums[i]

            for i in range(k):
                nums[n-k+i] = temp[i]

            return nums
        
# Example usage:
case1 = [1,2,3,4,5]
case2 = [10]
case3 = [7,8,9]
sol = Solution()
res1 = sol.rotateArray(case1, 8)
print("Array after left rotation by k for case1:", res1)  # Output: [3, 4, 5, 1, 2]
res2 = sol.rotateArray(case2, 3)
print("Array after left rotation by k for case2:", res2)  # Output:
res3 = sol.rotateArray(case3, 1)
print("Array after left rotation by k for case3:", res3)  # Output: [8, 9, 7]