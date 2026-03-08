"""
18. 4Sum
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

nums = [2,2,2,2,2]
target = 8

solution_array = set()

for index1 in range(0, len(nums)):
    for index2 in range(index1 + 1, len(nums)):
        for index3 in range(index2 + 1, len(nums)):
            for index4 in range(index3 + 1, len(nums)):
                if nums[index1] + nums[index2] + nums[index3] + nums[index4] == target:
                    solution_array.add((nums[index1], nums[index2], nums[index3], nums[index4]))
print(list(list(quad) for quad in solution_array))