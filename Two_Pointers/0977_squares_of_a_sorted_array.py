from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Problem Link: https://leetcode.com/problems/squares-of-a-sorted-array/
        
        Time Complexity: O(N) - Single pass using two pointers from both ends.
        Space Complexity: O(1) - Auxiliary space allocation (O(N) if output array is counted).
        
        Description:
        Since the input array is already sorted, the maximum squared values will always 
        reside either at the far-left (negative boundary) or far-right (positive boundary).
        We compare values from both ends using two pointers and populate the result array 
        from back to front (highest to lowest).
        """
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        pos = n - 1
        
        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2
            
            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1
            
        return result

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (LeetCode Example 1)
    test_input1 = [-4, -1, 0, 3, 10]
    expected1 = [0, 1, 9, 16, 100]
    result1 = sol.sortedSquares(test_input1)
    print(f"Test 1: {'PASSED ✅' if result1 == expected1 else 'FAILED ❌'}")
    print(f"Input: {test_input1} | Expected: {expected1} | Output: {result1}")
    print("-" * 50)