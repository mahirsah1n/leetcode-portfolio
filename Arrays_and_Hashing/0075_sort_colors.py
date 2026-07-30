from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Problem Link: https://leetcode.com/problems/sort-colors/
        
        Time Complexity: O(N) - Two linear passes over the array.
        Space Complexity: O(1) - Modifies the array in-place using constant auxiliary variables.
        
        Description:
        Two-pass Counting Sort approach:
        1. First pass counts the total frequencies of 0s, 1s, and 2s in the array.
        2. Second pass sequentially overwrites the array in-place with 0s, then 1s, and finally 2s.
        """
        count0 = 0
        count1 = 0
        count2 = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            elif nums[i] == 1:
                count1 += 1
            elif nums[i] == 2:
                count2 += 1
        
        for i in range(0, count0):
            nums[i] = 0

        for i in range(count0, count0 + count1):
            nums[i] = 1

        for i in range(count0 + count1, count0 + count1 + count2):
            nums[i] = 2

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (LeetCode Example 1)
    test_input1 = [2, 0, 2, 1, 1, 0]
    expected1 = [0, 0, 1, 1, 2, 2]
    sol.sortColors(test_input1)
    print(f"Test 1: {'PASSED ✅' if test_input1 == expected1 else 'FAILED ❌'}")
    print(f"Expected: {expected1} | Output: {test_input1}")
    print("-" * 50)
    
    # Test Case 2 (LeetCode Example 2)
    test_input2 = [2, 0, 1]
    expected2 = [0, 1, 2]
    sol.sortColors(test_input2)
    print(f"Test 2: {'PASSED ✅' if test_input2 == expected2 else 'FAILED ❌'}")
    print(f"Expected: {expected2} | Output: {test_input2}")
    print("-" * 50)