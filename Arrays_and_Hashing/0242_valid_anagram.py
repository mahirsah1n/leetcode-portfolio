from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Problem Link: https://leetcode.com/problems/valid-anagram/
        
        Time Complexity: O(N) - Building frequency maps for s and t of length N takes O(N) time.
        Space Complexity: O(K) - Extra space for character counts where K is the number of unique characters (O(1) if lowercase English alphabet).
        
        Description:
        Pythonic one-liner using `collections.Counter`.
        Builds character frequency maps for both strings `s` and `t` and checks if they are identical.
        """
        return Counter(s) == Counter(t)

if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)
    
    # Test Case 1 (Valid Anagram)
    test_s1, test_t1 = "anagram", "nagaram"
    expected1 = True
    result1 = sol.isAnagram(test_s1, test_t1)
    print(f"Test 1: {'PASSED ✅' if result1 == expected1 else 'FAILED ❌'}")
    print(f"Input: s = '{test_s1}', t = '{test_t1}' | Expected: {expected1} | Output: {result1}")
    print("-" * 50)
    
    # Test Case 2 (Invalid Anagram)
    test_s2, test_t2 = "rat", "car"
    expected2 = False
    result2 = sol.isAnagram(test_s2, test_t2)
    print(f"Test 2: {'PASSED ✅' if result2 == expected2 else 'FAILED ❌'}")
    print(f"Input: s = '{test_s2}', t = '{test_t2}' | Expected: {expected2} | Output: {result2}")
    print("-" * 50)