from typing import List

"""
LeetCode 2239: Find Closest Number to Zero
Link: https://leetcode.com/problems/find-closest-number-to-zero/

Description:
Given an integer array nums of size n, return the number with the value closest to 0 in nums.
If there are multiple answers, return the number with the largest value.

Approach:
Single-Pass Iteration:
1. Initialize `closest_number` with the first element of `nums`.
2. Iterate through the array `nums`:
   - If the absolute value of the current element is smaller than `abs(closest_number)`, 
     update `closest_number` to the current element.
   - If the absolute values are equal, update `closest_number` to `max(nums[i], closest_number)` 
     to ensure tie-breaking in favor of the larger value (e.g., choosing 1 over -1).
3. Return `closest_number`.

Complexity Analysis:
- Time Complexity: O(N) where N is the length of `nums`, as we traverse the list in a single loop.
- Space Complexity: O(1) auxiliary space as we only track a single state variable.
"""


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_number = nums[0]

        for i in range(len(nums)):
            if abs(nums[i]) < abs(closest_number):
                closest_number = nums[i]
            elif abs(nums[i]) == abs(closest_number):
                closest_number = max(nums[i], closest_number)

        return closest_number


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: nums = [-4, -2, 1, 4, 8] -> Expected: 1
    res1 = solution.findClosestNumber([-4, -2, 1, 4, 8])
    assert res1 == 1, f"Expected 1, got {res1}"

    # Test Case 2: nums = [2, -1, 1] -> Expected: 1
    res2 = solution.findClosestNumber([2, -1, 1])
    assert res2 == 1, f"Expected 1, got {res2}"

    # Test Case 3: nums = [-4, 2, -2] -> Expected: 2
    res3 = solution.findClosestNumber([-4, 2, -2])
    assert res3 == 2, f"Expected 2, got {res3}"

    print("All tests passed successfully!")