from typing import List
from collections import Counter

"""
LeetCode 347: Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/

Description:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Approach:
Frequency Map + Heap (`most_common`):
1. Count the frequency of each element in `nums` using `collections.Counter`.
2. Use `count.most_common(k)` which extracts the `k` highest frequency elements 
   (utilizing a heap under the hood).
3. Extract the element values (first item of each tuple) into the result list.

Complexity Analysis:
- Time Complexity: O(N log k) where N is the length of `nums`, as `most_common(k)`
  uses a heap to extract the top k elements.
- Space Complexity: O(N) to store element frequencies in the hash map.
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top_k = count.most_common(k)

        res = []
        for pair in top_k:
            res.append(pair[0])

        return res


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: nums = [1, 1, 1, 2, 2, 3], k = 2 -> Expected: [1, 2]
    res1 = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(res1) == [1, 2], f"Expected [1, 2], got {res1}"

    # Test Case 2: nums = [1], k = 1 -> Expected: [1]
    res2 = solution.topKFrequent([1], 1)
    assert res2 == [1], f"Expected [1], got {res2}"

    # Test Case 3: nums = [1, 2, 1, 2, 1, 3, 3, 2], k = 2 -> Expected: [1, 2]
    res3 = solution.topKFrequent([1, 2, 1, 2, 1, 3, 3, 2], 2)
    assert sorted(res3) == [1, 2], f"Expected [1, 2], got {res3}"

    print("All tests passed successfully!")