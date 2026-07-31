from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Problem Link: https://leetcode.com/problems/group-anagrams/
        
        Time Complexity: O(N * K log K) - N is the number of strings and K is the max string length.
        Space Complexity: O(N * K) - Memory used by the `groups` hash table.
        
        Description:
        Standard dictionary approach:
        We iterate through each word, construct a sorted character string as `key`,
        and check if it exists in `groups`. If absent, we initialize an empty list
        and append the original word.
        """
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
            
        return list(groups.values())

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (Standard LeetCode Example)
    test_input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = sol.groupAnagrams(test_input1)
    
    # Normalize order for verification
    normalized_result1 = sorted([sorted(group) for group in result1])
    expected1 = sorted([sorted(group) for group in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]])
    
    print(f"Test 1: {'PASSED ✅' if normalized_result1 == expected1 else 'FAILED ❌'}")
    print(f"Input: {test_input1} | Output: {result1}")
    print("-" * 50)
    
    # Test Case 2 (Single Empty String)
    test_input2 = [""]
    expected2 = [[""]]
    result2 = sol.groupAnagrams(test_input2)
    print(f"Test 2: {'PASSED ✅' if result2 == expected2 else 'FAILED ❌'}")
    print(f"Input: {test_input2} | Expected: {expected2} | Output: {result2}")
    print("-" * 50)