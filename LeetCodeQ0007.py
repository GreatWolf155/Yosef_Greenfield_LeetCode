"""
7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

Constraints:
-231 <= x <= 231 - 1
"""

sign = None
reversed_num = 0
while True:
    number = int(input("Input number: "))
    if not -231 < number < 230:
        print("Invalid number, not in range [-231, 230]")
        continue
    break
list_num = list(str(number))
if list_num[0] == '-':
    sign = -1
    list_num.remove('-')
else:
    sign = 1
for index in range(len(list_num)):
    reversed_num += int(list_num[index]) * (10 ** index)
reversed_num *= sign
if -231 < reversed_num < 230:
    print(reversed_num)
else:
    print(0)