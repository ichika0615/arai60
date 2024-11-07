class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        ans_idx = 0
        current = head

        while current is not None:
            if current in visited_nodes:
                return current
            visited_nodes.add(current)
            current = current.next
            ans_idx += 1
        return 

# ネーミングを改めた。
# 1発で解けた。嬉しい。
# returnに何を返せばいいのかわからず、ans_idxという謎の変数が初期化されている。普通にcurrentを返せばいい。

# Follow up: Can you solve it using O(1) (i.e. constant) memory?
# フロイドの循環検出も使えるかと思ったがよく考えれば難しい。文字通り循環を検出できるだけ。
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return
"""

#どこで出会うかなんてわからない。
#一応やり方はあるらしい


