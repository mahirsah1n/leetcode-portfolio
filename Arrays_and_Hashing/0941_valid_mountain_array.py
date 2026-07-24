"""
LeetCode 941: Valid Mountain Array
Link: https://leetcode.com/problems/valid-mountain-array/

Description:
Given an array of integers arr, return true if and only if it is a valid mountain array.

An array arr is a mountain array if and only if:
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Approach:
Single-Pass Simulation / Two Pointers.
1. Walk up the mountain from left to right as long as elements are strictly increasing.
2. Check if the peak is valid (it cannot be the first or the last element).
3. Walk down from the peak to the end, ensuring elements are strictly decreasing.
4. If we reach the end without encountering any flat or increasing step, return True.

Complexity Analysis:
- Time Complexity: O(N) - Single pass over the array of length N.
- Space Complexity: O(1) - Uses a constant amount of extra memory for pointer `i`.
"""

from typing import List


class Solution:

    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 0

        # Walk up (strictly increasing)
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        # Peak cannot be the first or last element
        if i == 0 or i == n - 1:
            return False

        # Walk down (strictly decreasing)
        while i < n - 1:
            if arr[i] <= arr[i + 1]:
                return False
            i += 1

        return True


# --- Local Test / Driver Code ---
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Valid Mountain
    arr1 = [0, 3, 2, 1]
    res1 = solution.validMountainArray(arr1)
    print("Test 1 Output:", res1)
    assert res1 is True, "Test 1 Failed!"

    # Test Case 2: Strictly Increasing (No peak)
    arr2 = [1, 2, 3, 4, 5]
    res2 = solution.validMountainArray(arr2)
    print("Test 2 Output:", res2)
    assert res2 is False, "Test 2 Failed!"

    # Test Case 3: Plateau / Duplicate values
    arr3 = [0, 2, 3, 3, 5, 2, 1, 0]
    res3 = solution.validMountainArray(arr3)
    print("Test 3 Output:", res3)
    assert res3 is False, "Test 3 Failed!"

    print("\n✅ All local test cases passed for LC 941!")