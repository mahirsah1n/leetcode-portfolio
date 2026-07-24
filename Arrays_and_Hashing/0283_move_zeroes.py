from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Problem Link: https://leetcode.com/problems/move-zeroes/
        
        Time Complexity: O(N) - Two sequential linear passes through the array.
        Space Complexity: O(1) - In-place modification without extra space.
        
        Description:
        Two-pass approach:
        1. First pass copies all non-zero elements to the front of the array at index `k`.
        2. Second pass fills all remaining positions from `k` to the end with zeroes.
        """
        k = 0
        
        # Pass 1: Shift non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
                
        # Pass 2: Fill remaining elements with zeroes
        for i in range(k, len(nums)):
            nums[i] = 0

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (Standard Example)
    test_input1 = [0, 1, 0, 3, 12]
    expected1 = [1, 3, 12, 0, 0]
    sol.moveZeroes(test_input1)
    print(f"Test 1: {'PASSED ✅' if test_input1 == expected1 else 'FAILED ❌'}")
    print(f"Expected: {expected1} | Output: {test_input1}")
    print("-" * 50)
    
    # Test Case 2 (Single Element Boundary Case)
    test_input2 = [0]
    expected2 = [0]
    sol.moveZeroes(test_input2)
    print(f"Test 2: {'PASSED ✅' if test_input2 == expected2 else 'FAILED ❌'}")
    print(f"Expected: {expected2} | Output: {test_input2}")
    print("-" * 50)