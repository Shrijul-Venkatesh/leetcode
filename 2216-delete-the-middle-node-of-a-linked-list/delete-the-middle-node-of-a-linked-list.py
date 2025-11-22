class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If list has only one node, delete it
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None
        
        # Move fast by 2 and slow by 1
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # slow is now the middle node → remove it
        prev.next = slow.next
        
        return head
