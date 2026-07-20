from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Problem Link: https://leetcode.com/problems/duplicate-zeros/
        
        Time Complexity: O(N) - Two linear passes over the array.
        Space Complexity: O(1) - Modifies the array in-place without extra space.
        
        Description:
        1. First Pass: Count the zeroes that can fit inside the original array bound
           and handle the edge case where a zero boundary gets cut off.
        2. Second Pass: Iterate backwards from the last valid element and shift
           elements rightwards, duplicating zeroes as required.
        """
        n = len(arr)
        count_dups = 0
        
        # Pass 1: Count zero duplicates that will fit within array bounds
        for i in range(n):
            if i > n - 1 - count_dups:
                break
            if arr[i] == 0:
                # Edge case: zero is at the edge and cannot be duplicated fully
                if i == n - 1 - count_dups:
                    arr[n - 1] = 0
                    n -= 1
                    break
                count_dups += 1
                
        # Pass 2: Shift elements backwards from the last valid index
        last = n - 1 - count_dups
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + count_dups] = 0
                count_dups -= 1
                arr[i + count_dups] = 0
            else:
                arr[i + count_dups] = arr[i]

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (In-Place Modification Check)
    test_input1 = [1, 0, 2, 3, 0, 4, 5, 0]
    expected1 = [1, 0, 0, 2, 3, 0, 0, 4]
    
    sol.duplicateZeros(test_input1)
    
    is_passed1 = test_input1 == expected1
    print(f"Test 1: {'PASSED ✅' if is_passed1 else 'FAILED ❌'}")
    print(f"Expected: {expected1} | Output: {test_input1}")
    print("-" * 50)