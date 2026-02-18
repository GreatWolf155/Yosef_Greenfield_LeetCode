"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

num1 = [2, 0, 2]
num2 = [3, 4, 5]

nums = sorted(num1 + num2)
middle = len(nums)//2
# print(middle)
# print(nums)
if len(nums) % 2 == 0:
    print((nums[middle] + nums[middle-1])/2)
else:
    print(nums[middle])

"""
# 4 line solution
if len(sorted(num1 + num2)) % 2 == 0:
    print((sorted(num1 + num2)[len(sorted(num1 + num2))//2] + sorted(num1 + num2)[len(sorted(num1 + num2))//2-1])/2)
else:
    print(sorted(num1 + num2)[len(sorted(num1 + num2))//2])
"""