"""
LeetCode 1346: Check If N and Its Double Exist
Link: https://leetcode.com/problems/check-if-n-and-its-double-exist/

Description:
Given an array arr of integers, check if there exist two indices i and j such that:
- i != j
- 0 <= i, j < arr.length
- arr[i] == 2 * arr[j]

Approach:
Hash Set (O(1) Lookup). As we iterate through the array, for each number x,
we check whether we have already seen its double (2 * x) or its half (x / 2, only if x is even).
If either exists in our set, a valid pair is found. Otherwise, we add x to the set.

Complexity Analysis:
- Time Complexity: O(N) - Single pass over the array of length N with average O(1) set operations.
- Space Complexity: O(N) - Memory allocated for storing up to N unique numbers in the set.
"""

from typing import List


class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)

        return False


# --- Local Test / Driver Code ---
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    arr1 = [10, 2, 5, 3]
    res1 = solution.checkIfExist(arr1)
    print("Test 1 Output:", res1)
    assert res1 is True, "Test 1 Failed!"

    # Test Case 2
    arr2 = [3, 1, 7, 11]
    res2 = solution.checkIfExist(arr2)
    print("Test 2 Output:", res2)
    assert res2 is False, "Test 2 Failed!"

    print("\n✅ All local test cases passed for LC 1346!")