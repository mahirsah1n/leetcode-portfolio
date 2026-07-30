from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Problem Link: https://leetcode.com/problems/height-checker/
        
        Time Complexity: O(N log N) - Due to sorting the heights array to create the expected order.
        Space Complexity: O(N) - Additional space allocated for the sorted array copy.
        
        Description:
        We create a sorted copy of the `heights` array representing the expected non-decreasing order.
        We then iterate through both arrays simultaneously to count the number of indices 
        where the actual height differs from the expected height.
        """
        expected = sorted(heights)
        mismatches = 0
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatches += 1
                
        return mismatches

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (LeetCode Example 1)
    test_input1 = [1, 1, 4, 2, 1, 3]
    expected1 = 3
    result1 = sol.heightChecker(test_input1)
    print(f"Test 1: {'PASSED ✅' if result1 == expected1 else 'FAILED ❌'}")
    print(f"Input: {test_input1} | Expected: {expected1} | Output: {result1}")
    print("-" * 50)
    
    # Test Case 2 (LeetCode Example 2)
    test_input2 = [5, 1, 2, 3, 4]
    expected2 = 5
    result2 = sol.heightChecker(test_input2)
    print(f"Test 2: {'PASSED ✅' if result2 == expected2 else 'FAILED ❌'}")
    print(f"Input: {test_input2} | Expected: {expected2} | Output: {result2}")
    print("-" * 50)