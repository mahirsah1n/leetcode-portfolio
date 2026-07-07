from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        Problem Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
        
        Time Complexity: O(N * K) - Where N is the number of elements and K is the average number of digits.
        Space Complexity: O(K) - Temporary space allocation for string conversion of digits.
        
        Description:
        We iterate through each number in the array, convert it to a string to determine 
        its digit length, and check if the length is divisible by 2.
        """
        even_digit_count = 0
        
        for num in nums:
            digit_length = len(str(num))
            if digit_length % 2 == 0:
                even_digit_count += 1
                
        return even_digit_count

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (LeetCode Example 1)
    test_input1 = [12, 345, 2, 6, 7896]
    expected1 = 2
    result1 = sol.findNumbers(test_input1)
    print(f"Test 1: {'PASSED ✅' if result1 == expected1 else 'FAILED ❌'}")
    print(f"Input: {test_input1} | Expected: {expected1} | Output: {result1}")
    print("-" * 50)