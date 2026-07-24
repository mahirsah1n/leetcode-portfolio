from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Problem Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
        
        Time Complexity: O(N) - Single pass from right to left.
        Space Complexity: O(1) - Modifies the array in-place without extra space.
        
        Description:
        We iterate through the array backwards starting from the last element.
        We maintain a running maximum variable initialized to -1.
        For each element, we temporarily store its original value, replace the element 
        with the current running maximum, and then update the maximum if the original 
        value was greater.
        """
        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_val
            if temp > max_val:
                max_val = temp
                
        return arr

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (LeetCode Example 1)
    test_input1 = [17, 18, 5, 4, 6, 1]
    expected1 = [18, 6, 6, 6, 1, -1]
    result1 = sol.replaceElements(test_input1[:])
    print(f"Test 1: {'PASSED ✅' if result1 == expected1 else 'FAILED ❌'}")
    print(f"Input: {test_input1} | Expected: {expected1} | Output: {result1}")
    print("-" * 50)
    
    # Test Case 2 (Single Element Boundary Case)
    test_input2 = [400]
    expected2 = [-1]
    result2 = sol.replaceElements(test_input2[:])
    print(f"Test 2: {'PASSED ✅' if result2 == expected2 else 'FAILED ❌'}")
    print(f"Input: {test_input2} | Expected: {expected2} | Output: {result2}")
    print("-" * 50)