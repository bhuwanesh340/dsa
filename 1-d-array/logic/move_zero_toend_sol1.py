'''
Docstring for 1-d-array.logic.move_zero_toend_sol1
'''

class Solution:
    def moveZeroes(self, nums):

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == 0:
                    # swap
                    if nums[j] != 0:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp

                    else:
                        continue
                else:
                    continue

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