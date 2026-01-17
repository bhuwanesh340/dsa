'''
Given an array of integers nums, return the value of the largest element in the array
'''

class Solution:
    def largestElement(self, nums):
        if type(nums) != list:
            temp_list = nums.split(",")
        
        largest = nums[0]

        if len(nums) > 1:
            for i in range(1,len(nums)):
                if nums[i] > largest:
                    largest = nums[i]

        return largest
    
case1 = [3, 5, 7, 2, 8]
case2 = [-10, -3, -1, -7]
case3 = [0, 0, 0, 0]
sol = Solution()
res1 = sol.largestElement(case1)
print("The largest number in the array is:", res1)
res2 = sol.largestElement(case2)
print("The largest number in the array is:", res2)
res3 = sol.largestElement(case3)
print("The largest number in the array is:", res3)