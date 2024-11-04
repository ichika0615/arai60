Python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        current = head

        while current:
            if current in hashset:
                return True
            hashset.add(current)
            current = current.next
        return False

#時間計算量はO(n) 空間計算量はO(n)
#Runtime: 45ms  Memory: 19.67MB

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#時間計算量O(n)  空間計算量O(1)
#Runtime: 35ms  Memory: 19.12MB (思ったよりメモリー変わらない)


