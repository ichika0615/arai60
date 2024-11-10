#一番好み。わかりやすい
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
                continue #下の処理はお預け
            current = current.next
        return head

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head 

        while current is not None:
            while current.next is not None and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head
  
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
            
        new_head = ListNode(head.val)
        new_current = new_head

        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
                continue
            current = current.next
            new_node = ListNode(current.val)
            new_current.next = new_node
            new_current = new_node
        return new_head

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        new_head = ListNode(head.val)
        new_current = new_head

        current = head

        while current is not None:
            while current.next is not None and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
            if current is None:
                return new_head 
            new_node = ListNode(current.val)
            new_current.next = new_node
            new_current = new_node
        return new_head
