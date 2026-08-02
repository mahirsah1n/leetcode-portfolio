from typing import List

"""
LeetCode 238: Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/

Description:
Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].
The algorithm must run in O(N) time complexity and without using the division operation.

Approach:
Prefix and Suffix Products (Two-Pass In-Place Accumulation):
1. Initialize an `answer` array of size N with 1s.
2. Left-to-Right Pass (Prefix): Accumulate prefix products. Assign `prefix` to `answer[i]`, 
   then multiply `prefix` by `nums[i]`.
3. Right-to-Left Pass (Suffix): Accumulate suffix products. Multiply `answer[i]` by `suffix`, 
   then multiply `suffix` by `nums[i]`.
4. Return `answer`.

Complexity Analysis:
- Time Complexity: O(N) where N is the length of `nums`, as it performs two linear passes.
- Space Complexity: O(1) auxiliary space, as the output array `answer` does not count towards space complexity per problem rules.
"""


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: nums = [1, 2, 3, 4] -> Expected: [24, 12, 8, 6]
    res1 = solution.productExceptSelf([1, 2, 3, 4])
    assert res1 == [24, 12, 8, 6], f"Expected [24, 12, 8, 6], got {res1}"

    # Test Case 2: nums = [-1, 1, 0, -3, 3] -> Expected: [0, 0, 9, 0, 0]
    res2 = solution.productExceptSelf([-1, 1, 0, -3, 3])
    assert res2 == [0, 0, 9, 0, 0], f"Expected [0, 0, 9, 0, 0], got {res2}"

    print("All tests passed successfully!")