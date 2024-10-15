"""Python

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        current = head 
        while current != None:
            if current in hashset:
                return True
            hashset.add(current)
            current = current.next
        
        return False

"""