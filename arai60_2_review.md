# ハッシュセットを使う
```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        visited_nodes = set()

        while current:
            if current in visited_nodes:
                return current
            visited_nodes.add(current)
            current = current.next
        
        return None
```
- tc O(n)
- sc O(n)

# Floydの循環検出法を応用

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                pointer_1 = slow
                pointer_2 = head
                while pointer_1 != pointer_2:
                    pointer_1 = pointer_1.next
                    pointer_2 = pointer_2.next
                return pointer_1
        
        return None
```
- tc O(n)
- sc O(1)



