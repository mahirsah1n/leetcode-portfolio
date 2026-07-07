from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Problem Link: https://leetcode.com/problems/max-consecutive-ones/
        
        Time Complexity: O(N) - Linear scan through the array exactly once.
        Space Complexity: O(1) - Only two integer variables used for tracking.
        
        Description:
        We iterate through the array maintaining a running count of consecutive 1s.
        Whenever we encounter a 1, we increment the current count and update the maximum global streak.
        When a 0 is found, the current consecutive streak resets to 0.
        """
        current_streak = 0
        max_streak = 0
        
        for num in nums:
            if num == 1:
                current_streak += 1
            else:
                current_streak = 0
                
            if current_streak > max_streak:
                max_streak = current_streak
                
        return max_streak

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (LeetCode Example 1)
    test_input1 = [1, 1, 0, 1, 1, 1]
    expected1 = 3
    result1 = sol.findMaxConsecutiveOnes(test_input1)
    print(f"Test 1: {'PASSED ✅' if result1 == expected1 else 'FAILED ❌'}")
    print(f"Input: {test_input1} | Expected: {expected1} | Output: {result1}")
    print("-" * 50)