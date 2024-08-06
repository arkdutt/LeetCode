# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #find the middle node -> use fast and slow pointers
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #seperate the list into 2 halves
        half = slow.next
        slow.next = None

        #reverse the second half of the seperated list
        curr = half
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #merge both the lists as given by the question
        first = head
        second = prev

        while second:
            list1 = first.next
            list2 = second.next

            first.next = second
            second.next = list1

            first = list1
            second = list2


        #Time Complexity: O(N) [Combining all the steps = O(n) + O(n) + O(n) = O(n)]
        #Space Complexity: O(1) since we are only using a few pointers and no additional data structures relative to the input size