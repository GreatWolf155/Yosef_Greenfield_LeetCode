"""
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it
becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

number = int(input("input number to check for palindrome: "))

# convert to string method:
if list(str(number)) == list(str(number))[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# no conversion method
check = 0
number_test = number
while number_test:
    check = check * 10 + number_test % 10
    number_test = number_test // 10
if check == number:
    print("palindrome")
else:
    print("not palindrome")
