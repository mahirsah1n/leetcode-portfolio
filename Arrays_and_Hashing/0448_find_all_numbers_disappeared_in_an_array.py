from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Problem Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
        
        Time Complexity: O(N) - O(N) to construct set + O(N) loop through range(1, n + 1).
        Space Complexity: O(N) - Additional space allocated for the hash set.
        
        Description:
        We store the unique elements of `nums` in a hash set to allow O(1) membership lookups.
        We then iterate through the range from 1 to N, appending any number missing from the set
        to our result list.
        """
        n = len(nums)
        nums_set = set(nums)
        missing_numbers = []
        
        for num in range(1, n + 1):
            if num not in nums_set:
                missing_numbers.append(num)
                
        return missing_numbers

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (LeetCode Example 1)
    test_input1 = [4, 3, 2, 7, 8, 2, 3, 1]
    expected1 = [5, 6]
    result1 = sol.findDisappearedNumbers(test_input1)
    print(f"Test 1: {'PASSED ✅' if result1 == expected1 else 'FAILED ❌'}")
    print(f"Input: {test_input1} | Expected: {expected1} | Output: {result1}")
    print("-" * 50)
    
    # Test Case 2 (LeetCode Example 2)
    test_input2 = [1, 1]
    expected2 = [2]
    result2 = sol.findDisappearedNumbers(test_input2)
    print(f"Test 2: {'PASSED ✅' if result2 == expected2 else 'FAILED ❌'}")
    print(f"Input: {test_input2} | Expected: {expected2} | Output: {result2}")
    print("-" * 50)