from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Problem Link: https://leetcode.com/problems/sort-array-by-parity/
        
        Time Complexity: O(N) - Single pass through the array.
        Space Complexity: O(1) - In-place array modification without extra memory.
        
        Description:
        Two-pointer partition technique:
        `l` maintains the boundary of even numbers, while `r` scans through the array.
        Whenever an even number (nums[r] % 2 == 0) is encountered, it is swapped 
        with the element at `l`, and `l` is incremented.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (Standard Example)
    test_input1 = [3, 1, 2, 4]
    result1 = sol.sortArrayByParity(test_input1[:])
    
    # Verification: Check if all even numbers precede odd numbers
    even_part = [x for x in result1 if x % 2 == 0]
    odd_part = [x for x in result1 if x % 2 != 0]
    is_valid1 = result1 == even_part + odd_part
    
    print(f"Test 1: {'PASSED ✅' if is_valid1 else 'FAILED ❌'}")
    print(f"Input: [3, 1, 2, 4] | Output: {result1}")
    print("-" * 50)
    
    # Test Case 2 (Single Element Boundary Case)
    test_input2 = [0]
    expected2 = [0]
    result2 = sol.sortArrayByParity(test_input2[:])
    print(f"Test 2: {'PASSED ✅' if result2 == expected2 else 'FAILED ❌'}")
    print(f"Expected: {expected2} | Output: {result2}")
    print("-" * 50)