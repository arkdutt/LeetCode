# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, slow and fast, both starting at the head of the list
        slow = head
        fast = head

        # Traverse the list with the fast pointer moving twice as fast as the slow pointer
        while fast and fast.next:
            # Move the fast pointer two steps ahead
            fast = fast.next.next
            # Move the slow pointer one step ahead
            slow = slow.next
            # If the fast pointer meets the slow pointer, there is a cycle
            if fast == slow:
                return True
        # If the loop terminates without the pointers meeting, there is no cycle
        return False
    
    #Time Complexity: O(n) where n is the number of nodes in a list
    #Space Complexity: O(1) since we are only using 2 pointers, the algo uses a fixed amount of space