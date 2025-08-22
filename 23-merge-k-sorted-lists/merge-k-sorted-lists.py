# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq                              # min-heap for picking smallest head among k lists
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        # edge case, no lists given
        if not lists:
            return None

        heap = []                         # will hold tuples (value, unique_id, node)
        uid = 0                           # unique counter to avoid comparing nodes on tie

        # push head of each non-empty list into heap
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, uid, node))
                uid += 1

        dummy = ListNode(0)               # dummy head to build result list
        tail = dummy                      # tail pointer for appending nodes

        # repeatedly extract smallest node and push its next
        while heap:
            val, _, node = heapq.heappop(heap)  # get node with smallest value
            tail.next = node                     # append to result
            tail = tail.next                     # move tail
            if node.next:                        # if list continues, push next node
                heapq.heappush(heap, (node.next.val, uid, node.next))
                uid += 1

        return dummy.next                # head of merged sorted list
        