from typing import List


class Solution:
    """
    Problem Link: https://leetcode.com/problems/longest-consecutive-sequence/

    Time Complexity: O(N) - Converting list to set takes O(N). Each number is only
                     processed in the while loop if it's the start of a sequence,
                     visiting each element at most twice.
    Space Complexity: O(N) - Storing unique numbers in a hash set.

    Description:
    Given an unsorted array of integers nums, return the length of the longest
    consecutive elements sequence. An algorithm that runs in O(n) time is required.
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting if 'num' is the first number of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest


if __name__ == "__main__":
    sol = Solution()
    print("=" * 50)
    print("RUNNING LOCAL INTEGRATION TESTS...")
    print("=" * 50)

    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
        ([], 0),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        output = sol.longestConsecutive(nums)
        status = "PASSED ✅" if output == expected else "FAILED ❌"
        print(f"\nTest {i}: {status}")
        print(f"Input: {nums} | Expected: {expected} | Output: {output}")
        assert output == expected, f"Test {i} Failed: expected {expected}, got {output}"