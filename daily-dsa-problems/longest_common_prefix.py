'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

class Solution:  
    def longestCommonPrefix(self, st : str) -> str:
        #your code goes here
        if not st:
            return ""
        st.sort()

        # print(st)

        first_ele = st[0]
        last_ele = st[-1]

        ans = []

        for i in range(min(len(first_ele), len(last_ele))):
            if first_ele[i] != last_ele[i]:
                return ''.join(ans)
            
            ans.append(first_ele[i])

        return ''.join(ans)

# Example usage:
case1 = ["flower","flow","flight"]

case2 = ["dog","racecar","car"]
sol = Solution()
res1 = sol.longestCommonPrefix(case1)
print("The longest common prefix is:", res1)
res2 = sol.longestCommonPrefix(case2)
print("The longest common prefix is:", res2)