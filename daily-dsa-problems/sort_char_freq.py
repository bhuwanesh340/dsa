'''
You are given a string s. Return the array of unique characters, sorted by highest to lowest occurring characters.
If two or more characters have same frequency then arrange them in alphabetic order.
'''

class Solution:
    def frequencySort(self, s):
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1

        # Sort by frequency (descending) and then by character (ascending)
        sorted_chars = sorted(freq_map.items(), key=lambda x: (-x[1], x[0]))

        # Extract only the characters in the required order
        result = [char for char, freq in sorted_chars]
        return result
    
# Example usage:
case1 = "tree"
case2 = "cccaaa"
case3 = "Aabb"
sol = Solution()
res1 = sol.frequencySort(case1)
print("Sorted characters by frequency for case1:", res1)  # Output: ['e', 'r', 't']
res2 = sol.frequencySort(case2)
print("Sorted characters by frequency for case2:", res2)  # Output: ['a', 'c']
res3 = sol.frequencySort(case3)
print("Sorted characters by frequency for case3:", res3)  # Output: ['b', 'A', 'a']