# ハッシュセットを使う

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
- time complexity O(n)
- space complexity O(n)


# Floydの循環検出法

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode], visited_nodes = None) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
```
- tc O(n)
- sc O(1)
まあ、ネタ程度に知っていればいいんじゃない？

# 再帰

- pythonの再帰呼び出し可能回数はデフォルトで1000回で、制約条件によるとノードの最大数は10**4
- sys.setrecursionlimit()で調節しておいた。

```python
import sys 
sys.setrecursionlimit(10**5)

class Solution:
    def hasCycle(self, head: Optional[ListNode], visited_nodes = None) -> bool:
        def _has_cycle(current, visited_nodes):
            if current is None:
                return False
            if current in visited_nodes:
                return True
            visited_nodes.add(current)
            return _has_cycle(current.next, visited_nodes)
        return _has_cycle(head, set())
```

再帰はまだ完全に消化できていないので、復習していきたい。
