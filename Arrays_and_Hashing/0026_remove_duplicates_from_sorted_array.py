"""
LeetCode 26: Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Description:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. Return the number of unique elements in nums.

Approach:
Two Pointers. Since the array is already sorted, duplicate values will always be adjacent.
We maintain a write pointer `b` (starting at index 1) and iterate through the array from index 1.
Whenever `nums[i] != nums[i - 1]`, we place `nums[i]` at `nums[b]` and increment `b`.

Complexity Analysis:
- Time Complexity: O(N) - Single pass through the array of length N.
- Space Complexity: O(1) - Modifies the array in-place without extra memory allocation.
"""

from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        b = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[b] = nums[i]
                b += 1
        return b


# --- Local Test / Driver Code ---
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    print(f"Test 1 Output: k = {k1}, nums = {nums1[:k1]}")
    assert k1 == 2, "Test 1 Failed: Length mismatch!"
    assert nums1[:k1] == [1, 2], "Test 1 Failed: Content mismatch!"

    # Test Case 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    print(f"Test 2 Output: k = {k2}, nums = {nums2[:k2]}")
    assert k2 == 5, "Test 2 Failed: Length mismatch!"
    assert nums2[:k2] == [0, 1, 2, 3, 4], "Test 2 Failed: Content mismatch!"

    print("\n✅ All local test cases passed for LC 26!")