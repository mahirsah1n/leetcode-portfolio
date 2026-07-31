from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Problem Link: https://leetcode.com/problems/two-sum/
        
        Time Complexity: O(N) - Single pass over the array with O(1) average hash map lookups.
        Space Complexity: O(N) - Additional space allocated for the `seen` hash map.
        
        Description:
        One-pass Hash Table approach:
        We iterate through `nums` while keeping track of each element and its index in a hash map (`seen`).
        For every element, we calculate its complement (`x = target - nums[i]`).
        If the complement already exists in `seen`, we return the pair of indices [seen[x], i].
        Otherwise, we insert the current element into `seen`.
        """
        seen = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in seen:
                return [seen[x], i]
            seen[nums[i]] = i

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (LeetCode Example 1)
    test_input1, target1 = [2, 7, 11, 15], 9
    expected1 = [0, 1]
    result1 = sol.twoSum(test_input1, target1)
    print(f"Test 1: {'PASSED ✅' if result1 == expected1 else 'FAILED ❌'}")
    print(f"Input: nums = {test_input1}, target = {target1} | Expected: {expected1} | Output: {result1}")
    print("-" * 50)
    
    # Test Case 2 (LeetCode Example 2)
    test_input2, target2 = [3, 2, 4], 6
    expected2 = [1, 2]
    result2 = sol.twoSum(test_input2, target2)
    print(f"Test 2: {'PASSED ✅' if result2 == expected2 else 'FAILED ❌'}")
    print(f"Input: nums = {test_input2}, target = {target2} | Expected: {expected2} | Output: {result2}")
    print("-" * 50)