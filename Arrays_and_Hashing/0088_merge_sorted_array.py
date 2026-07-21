"""
LeetCode 88: Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/

Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums2 into nums1 as one sorted array in-place.

Approach:
Backwards Two Pointers. Merging from left to right would overwrite unprocessed elements in nums1.
Therefore, we compare elements starting from the end (largest values) and place them 
at the end of nums1 in the available empty slots.

Complexity Analysis:
- Time Complexity: O(m + n) - Each element from nums1 and nums2 is processed at most once.
- Space Complexity: O(1) - The merge is performed in-place without allocating extra space.
"""

from typing import List


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Do not return anything, modify nums1 in-place instead."""
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # Fill nums1 with remaining elements from nums2 if any
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1


# --- Local Test / Driver Code ---
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1_test1 = [1, 2, 3, 0, 0, 0]
    m_test1 = 3
    nums2_test1 = [2, 5, 6]
    n_test1 = 3

    solution.merge(nums1_test1, m_test1, nums2_test1, n_test1)
    print("Test 1 Output:", nums1_test1)
    assert nums1_test1 == [1, 2, 2, 3, 5, 6], "Test 1 Failed!"

    # Test Case 2
    nums1_test2 = [1]
    m_test2 = 1
    nums2_test2 = []
    n_test2 = 0

    solution.merge(nums1_test2, m_test2, nums2_test2, n_test2)
    print("Test 2 Output:", nums1_test2)
    assert nums1_test2 == [1], "Test 2 Failed!"

    print("\n✅ All local test cases passed successfully!")