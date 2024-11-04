# 1
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
                continue
            current = current.next
        
        return head
```
- 2つずつ見ていって、重複してたら2個目を取り外していく。

# 2
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head
```
- ノードを1つ見て、ノード.next以降のやつも同じだったら取り外す。気が済むまでやる。

# 関数切り出し
- 隣と重複しているか確認する
- 1: 重複してないなら見るノードを移動する。
- 2: 重複しているなら重複しなくなるまでノードを削除する。
- これらのアルゴリズムを1つ1つ関数化する気持ちで。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def next_duplicated(node) -> bool:
            return node.next and node.val == node.next.val
        
        def skip_nodes(node, val_to_skip):
            while node and node.val == val_to_skip:
                node = node.next
            return node
        
        current = head
        while current:
            if next_duplicated(current):
                current.next = skip_nodes(current, current.val)
            current = current.next
        return head
```

# Wrong Answer
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def next_duplicated(node):
            return node and node.next and node.val == node.next.val
        
        def skip_nodes(node, val_to_skip):
            while node:
                if node.val == val_to_skip:
            return node
            # ↑一生終わらない
        
        current = head
        while current:
            if next_duplicated(current):
                current.next = skip_nodes(current.next, current.val)
                continue #continueいらない。
            current = current.next

        return head
```
