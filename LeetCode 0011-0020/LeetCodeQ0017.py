"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

map = {
    2: ['A', 'B', 'C']
    3: ['D', 'E', 'F']
    4: ['G', 'H', 'I']
    5: ['J', 'K', 'L']
    6: ['M', 'N', 'O']
    7: ['P', 'Q', 'R', 'S']
    8: ['T', 'U', 'V']
    9: ['W', 'X', 'Y', 'Z']


Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = "2"
Output: ["a","b","c"]


Constraints:
1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

map = {
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z']}

solution_array = [""]
digits = "235"

for num in digits:
    temp_array = []
    for item in solution_array:
        for letter in map[int(num)]:
            temp_array.append(item + letter)
    solution_array = temp_array
print(solution_array)
