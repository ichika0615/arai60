# Step1
- 新しく所望の連結リストを作る or 既存の連結リストを改造して所望の連結リストを得る
- 新しく連結リストを作る。
- headからノードを順に走査していき、その値と値の出現回数をハッシュテーブルに記録する。次にそのハッシュテーブルを走査して、出現回数が1の値のノードを作ってつなぎ、連結リストを得る。

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], visited_nodes=None) -> Optional[ListNode]:
        node_vals_freq = {}
        current = head

        while current:
            node_vals_freq[current.val] = 1 + node_vals_freq.get(current.val, 0)
            current = current.next

        dummy = ListNode()
        distinct_list = dummy

        for val, frequency in node_vals_freq.items():
            if frequency == 1:
                distinct_list.next = ListNode(val)
                distinct_list = distinct_list.next
        
        return dummy.next
```

- 既存の連結リストを改造する
- 先頭から走査していって、削除するべきノード(隣のノードと値が同じ)があったら、削除する値(val_to_delete)である間は削除し続ける。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], visited_nodes=None) -> Optional[ListNode]:
        current = head
        dummy = ListNode()
        distinct_list = dummy

        while current:
            if current.next and current.val == current.next.val:
                val_to_delete = current.val
                while current and current.val == val_to_delete:
                    current = current.next
                continue
            distinct_list.next = current
            distinct_list = distinct_list.next
            current = current.next
            
        distinct_list.next = None

        return dummy.next
```
# Step2
- 他の方のコードを見たりする。
- ノードの切り替えを関数で切り出す
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], visited_nodes=None) -> Optional[ListNode]:

        def skip_till_value_changes(current_node) -> Optional[ListNode]:
            #current_nodeから値が変わるまで隣のノードを参照し続ける
            while current_node.next and current_node.val == current_node.next.val:
                current_node = current_node.next
            return current_node.next

        current = head
        dummy = ListNode()
        distinct_list = dummy

        while current:
            if current.next and current.val == current.next.val:
                current = skip_till_value_changes(current)
                continue
            distinct_list.next = current
            distinct_list = distinct_list.next
            current = current.next

        distinct_list.next = None
        return dummy.next
```
- return current_node.nextがキモいなら、これでもいい。
```python
def skip_until_value_changes(current_node) -> Optional[ListNode]:
            # skips until a node value changes and returns a first node with a different value
            val_to_delete = current_node.val
            while current_node and current_node.val == val_to_delete:
                current_node = current_node.next
            return current_node
```

