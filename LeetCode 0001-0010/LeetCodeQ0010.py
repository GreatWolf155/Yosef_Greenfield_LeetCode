"""
10. Regular Expression Matching
Given an input string s and a pattern p, implement regular
expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there
will be a previous valid character to match.
"""

"""
s[i] == c[i] or s[i] == '.'

'.' = True
'*' means the previous input works any number of times
"""
s = 'adsdfgjks'
p = 'a..df.jks'
list_s = list(s)
list_p = list(p)
solution_list = []

if '*' not in list_p:
    for index in range(len(list_s)):
        if list_s[index] == list_p[index] or list_p[index] == '.':
            solution_list.append(True)
        else:
            solution_list.append(False)
            break
else:
    for index in range(len(list_s)):
        if list_s[index] == list_p[index] or list_p[index] == '.':
            solution_list.append(True)
        elif list_p[index] == '*':
            # run through list_p and list_s to search until the next 'DIFFERENT' letter
            #look at index -1, run until list_s has a different value than that
            check = list_p[index - 1]
            i = index
            while check == list_p[i]:



            # figure out what to do for a dot before it

            # figure out what to do for a dot after it

        else:
            solution_list.append(False)
            break



print(solution_list)


if False in solution_list:
    print("False")
else:
    print("True")