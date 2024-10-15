class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set() # set of nodes pointer already visited
        current = head

        while current != None:
            if current in hashset:
                return True
            hashset.add(current)
            current = current.next
        return False

#時間計算量はO(n) 空間計算量はO(n)

