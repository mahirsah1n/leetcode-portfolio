from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Problem Link: https://leetcode.com/problems/contains-duplicate/
        
        Time Complexity: O(N) - Building the Counter frequency map takes linear time.
        Space Complexity: O(N) - Additional space allocated for the Counter hash map.
        
        Description (Primary Approach - Frequency Map via Counter):
        Count the occurrences of each element using `collections.Counter`.
        Iterate through the keys, and if any number has a count >= 2, return True.
        """
        count = Counter(nums)

        for num in count:
            if count[num] >= 2:
                return True
        return False

    def containsDuplicateOneLiner(self, nums: List[int]) -> bool:
        """
        Alternative Approach (Approach 2 - Set Length Comparison):
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Compares the length of the original list with the length of its set representation.
        """
        return len(nums) != len(set(nums))

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (Contains Duplicates)
    test_input1 = [1, 2, 3, 1]
    expected1 = True
    result1 = sol.containsDuplicate(test_input1)
    result1_alt = sol.containsDuplicateOneLiner(test_input1)
    print(f"Test 1 (Primary Counter): {'PASSED ✅' if result1 == expected1 else 'FAILED ❌'}")
    print(f"Test 1 (Alternative One-Liner): {'PASSED ✅' if result1_alt == expected1 else 'FAILED ❌'}")
    print(f"Input: {test_input1} | Expected: {expected1} | Output: {result1}")
    print("-" * 50)
    
    # Test Case 2 (All Unique Elements)
    test_input2 = [1, 2, 3, 4]
    expected2 = False
    result2 = sol.containsDuplicate(test_input2)
    result2_alt = sol.containsDuplicateOneLiner(test_input2)
    print(f"Test 2 (Primary Counter): {'PASSED ✅' if result2 == expected2 else 'FAILED ❌'}")
    print(f"Test 2 (Alternative One-Liner): {'PASSED ✅' if result2_alt == expected2 else 'FAILED ❌'}")
    print(f"Input: {test_input2} | Expected: {expected2} | Output: {result2}")
    print("-" * 50)