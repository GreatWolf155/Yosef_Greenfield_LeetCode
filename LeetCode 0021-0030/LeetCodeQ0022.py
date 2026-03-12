"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]


Constraints:
1 <= n <= 8
"""
n = 1
parentheses = ['(', ')']
# Format: ( (permutation_sequence), open_count, close_count )
permutations = {( (), 0, 0)}
for _ in range(2 * n):
    bucket = set()
    for sequence, open_count, close_count in permutations:
        if open_count < n:
            bucket.add((sequence + (parentheses[0],), open_count + 1, close_count))
        if close_count < open_count:
            bucket.add((sequence + (parentheses[1],), open_count, close_count + 1))
    permutations = bucket
output = []
for p in permutations:
    output.append("".join(p[0]))
print(output)

