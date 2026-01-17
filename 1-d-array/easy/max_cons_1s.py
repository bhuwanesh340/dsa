'''
Given a binary array nums, return the maximum number of consecutive 1s in the array.
A binary array is an array that contains only 0s and 1s.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_sum = 0
        current = 0
        for i in nums:
            if i == 1:
                current += 1
            else:
                current = 0

            if current > max_sum:
                max_sum = current

        # print("max length of 1: ", max_sum)
        # print("prefix_sum: ", prefix_sum)

        return max_sum
    
# Example usage:
case1 = [1,1,0,1,1,1]
case2 = [1,0,1,1,0,1]
sol = Solution()
res1 = sol.findMaxConsecutiveOnes(case1)
print("Max consecutive 1s for case1:", res1)  # Output:
res2 = sol.findMaxConsecutiveOnes(case2)
print("Max consecutive 1s for case2:", res2)  # Output:

