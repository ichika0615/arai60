```python
class Solution:
    def hasCycle(self, head: Optional[ListNode], visited_nodes = None) -> bool:
        current = head
        visited_nodes = set()

        while current:
            if current in visited_nodes:
                return True
            visited_nodes.add(current)
            current = current.next
        
        return False
```

