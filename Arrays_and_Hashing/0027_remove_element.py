"""
LeetCode 27: Remove Element
Link: https://leetcode.com/problems/remove-element/

Description:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Approach:
Two Pointers (Fast & Slow Pointers). We iterate through the array with a fast pointer `i`.
Whenever `nums[i]` is not equal to `val`, we copy `nums[i]` to `nums[k]` and increment `k`.

Complexity Analysis:
- Time Complexity: O(N) - Single pass through the array of length N.
- Space Complexity: O(1) - Modifies the array in-place without extra space.
"""

from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


# --- Local Test / Driver Code ---
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print(f"Test 1 Output: k = {k1}, nums = {nums1[:k1]}")
    assert k1 == 2, "Test 1 Failed: Length mismatch!"
    assert sorted(nums1[:k1]) == [2, 2], "Test 1 Failed: Content mismatch!"

    # Test Case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(f"Test 2 Output: k = {k2}, nums = {nums2[:k2]}")
    assert k2 == 5, "Test 2 Failed: Length mismatch!"
    assert sorted(nums2[:k2]) == [0, 0, 1, 3, 4], (
        "Test 2 Failed: Content mismatch!"
    )

    print("\n✅ All local test cases passed for LC 27!")