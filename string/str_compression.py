"""
String Compression

Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.

Input Format
In the function a vector of characters is passed.

Output Format
Return the updated vector

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""



def compress(chars):
    count_dict = {}
    for char in chars:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    print("\nCount Dictionary:", count_dict)
    compressed_chars = []
    for char, count in count_dict.items():
        compressed_chars.append(char)
        if count > 1:
            compressed_chars.extend(list(str(count)))

    # Update the original chars list with compressed characters
    for i in range(len(compressed_chars)):
        if i < len(chars):
            chars[i] = compressed_chars[i]
        else:
            chars.append(compressed_chars[i])

    # Return the new length of the chars list
    return compressed_chars, len(compressed_chars)

# Example usage
# chars = ["a","a","b","b","c","c","c"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b", "c","c","c"]
compressed_chars, new_length = compress(chars)
print("Compressed characters:", compressed_chars)
print("New length of chars:", new_length)
print("chars after compression:", chars)