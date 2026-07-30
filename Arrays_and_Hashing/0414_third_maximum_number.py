from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        Problem Link: https://leetcode.com/problems/third-maximum-number/
        
        Time Complexity: O(N log N) - Converting to set takes O(N) and sorting unique elements takes O(N log N).
        Space Complexity: O(N) - Additional space allocated for the set and sorted list.
        
        Description:
        1. Remove duplicates by converting the array into a hash set.
        2. Sort the unique elements in descending order.
        3. Return the element at index 2 if there are at least 3 distinct values; 
           otherwise, return the maximum element at index 0.
        """
        nums = set(nums)
        nums = sorted(nums, reverse=True)
        
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (Standard 3rd max exists)
    test_input1 = [3, 2, 1]
    expected1 = 1
    result1 = sol.thirdMax(test_input1)
    print(f"Test 1: {'PASSED ✅' if result1 == expected1 else 'FAILED ❌'}")
    print(f"Input: {test_input1} | Expected: {expected1} | Output: {result1}")
    print("-" * 50)
    
    # Test Case 2 (3rd max does not exist, returns max)
    test_input2 = [1, 2]
    expected2 = 2
    result2 = sol.thirdMax(test_input2)
    print(f"Test 2: {'PASSED ✅' if result2 == expected2 else 'FAILED ❌'}")
    print(f"Input: {test_input2} | Expected: {expected2} | Output: {result2}")
    print("-" * 50)
    
    # Test Case 3 (Duplicates present)
    test_input3 = [2, 2, 3, 1]
    expected3 = 1
    result3 = sol.thirdMax(test_input3)
    print(f"Test 3: {'PASSED ✅' if result3 == expected3 else 'FAILED ❌'}")
    print(f"Input: {test_input3} | Expected: {expected3} | Output: {result3}")
    print("-" * 50)