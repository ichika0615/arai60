class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        current = head

        while current is not None:
            if current in visited_nodes:
                return current
            visited_nodes.add(current)
            current = current.next
        return

# 141(arai60_1)とほとんど変わらない。
# フロイドもできるらしいが、よくわからなかった。


