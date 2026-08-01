from typing import List, Optional

"""
LeetCode 206: Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/

Description:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Approach:
Iterative Two-Pointer Approach:
1. Maintain two pointers: `prev` initialized to None and `curr` initialized to head.
2. Traverse through the list:
   - Save `curr.next` in a temporary variable (`next_node`).
   - Reverse the link by setting `curr.next = prev`.
   - Move `prev` to `curr` and `curr` to `next_node`.
3. Return `prev` as the new head of the reversed linked list.

Complexity Analysis:
- Time Complexity: O(N) where N is the number of nodes in the linked list (single pass).
- Space Complexity: O(1) auxiliary space as reversal is done in-place.
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


# Helper functions for local driver code
def list_to_linkedlist(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: [1, 2, 3, 4, 5] -> Expected: [5, 4, 3, 2, 1]
    head1 = list_to_linkedlist([1, 2, 3, 4, 5])
    reversed_head1 = solution.reverseList(head1)
    res1 = linkedlist_to_list(reversed_head1)
    assert res1 == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], got {res1}"

    # Test Case 2: [1, 2] -> Expected: [2, 1]
    head2 = list_to_linkedlist([1, 2])
    reversed_head2 = solution.reverseList(head2)
    res2 = linkedlist_to_list(reversed_head2)
    assert res2 == [2, 1], f"Expected [2, 1], got {res2}"

    # Test Case 3: [] -> Expected: []
    head3 = list_to_linkedlist([])
    reversed_head3 = solution.reverseList(head3)
    res3 = linkedlist_to_list(reversed_head3)
    assert res3 == [], f"Expected [], got {res3}"

    print("All tests passed successfully!")