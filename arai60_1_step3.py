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

