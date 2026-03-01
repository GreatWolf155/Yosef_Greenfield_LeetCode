"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

strs = ["flower","flow","flight"]
longest_common_prefix = ""
for i in range(len(min(strs, key=len))):
    # if all index i in each string s in strs is equal to the i index of the first string in strs
    if all(s[i] == strs[0][i] for s in strs):
        longest_common_prefix += strs[0][i]
    else:
        break
print(longest_common_prefix)