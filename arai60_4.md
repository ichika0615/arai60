# Step1
- 新しく所望の連結リストを作る or 既存の連結リストを改造して所望の連結リストを得る
## 新しく連結リストを作る。 
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
- tc:O(n)/ sc:O(n)

## 既存の連結リストを改造する
- 先頭から走査していって、削除するべきノード(隣のノードと値が同じ)があったら、削除する値(val_to_delete)として保存。走査してval_to_deleteである間は削除し続ける。
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
- tc:O(n)/ sc:O(1)

# Step2
- 他の方のコードを見たりする。
## ノードの切り替えを関数で切り出す
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
- tc:O(n)/ sc:O(1)
- return current_node.nextがキモいなら、これでもいい。
```python
def skip_until_value_changes(current_node) -> Optional[ListNode]:
            # skips until a node value changes and returns a first node with a different value
            val_to_delete = current_node.val
            while current_node and current_node.val == val_to_delete:
                current_node = current_node.next
            return current_node
```
## 再帰
- 再帰の深さは最大、ノードの長さN。制約条件ではリストは最大300の長さなので、十分に再帰で実装できる。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], visited_nodes=None) -> Optional[ListNode]:
        # 再帰関数にやって欲しいこと：重複しているノードを消す。重複してないやつはそのまま残す。

        #停止条件
        if not head or not head.next:
            return head

        # 重複したノードを取り消す
        if head.next and head.val == head.next.val:
            val_to_delete = head.val
            while head and head.val == val_to_delete:
                head = head.next
            return self.deleteDuplicates(head)
        
        # 重複してないノードは残しておく。
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
```
- なかなか腑に落ちず、難しく感じた。

# Step 3
## 先頭から走査していって、削除するべきノード(隣のノードと値が同じ)があったら、削除する値(val_to_delete)として保存。走査してval_to_deleteである間は削除し続ける。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], visited_nodes=None) -> Optional[ListNode]:
        dummy = ListNode()
        distinct_list = dummy
        current = head

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
- tc:O(n)/ sc:O(1)

## 関数切り出し
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], visited_nodes=None) -> Optional[ListNode]:
        def skip_until_value_changes(current_node) -> Optional[ListNode]:
            # skips until a node value changes and returns a node with a different value
            val_to_delete = current_node.val
            while current_node and current_node.val == val_to_delete:
                current_node = current_node.next
            return current_node
        
        # We are going to make a linked list from scratch, so preparing a dummy node is a good idea.
        dummy = ListNode(-1000)
        distinct_list = dummy
        current = head

        while current:
            if current.next and current.val == current.next.val:
                current = skip_until_value_changes(current)
                continue
            distinct_list.next = current
            distinct_list = distinct_list.next
            current = current.next
        
        distinct_list.next = None

        return dummy.next
```
- tc:O(n)/ sc:O(1)

## 一重ループで申し送る。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], visited_nodes=None) -> Optional[ListNode]:
        dummy = ListNode()
        distinct_list = dummy
        current = head
        val_to_delete = None

        while current:
            if current.val == val_to_delete:
                current = current.next
                continue
            if current.next and current.val == current.next.val:
                val_to_delete = current.val
                continue
            distinct_list.next = current
            distinct_list = distinct_list.next
            current = current.next
        
        distinct_list.next = None

        return dummy.next
```
- tc:O(n)/ sc:O(1)

- このコードを上側に持ってくると永遠に足踏みする。一回間違えた。
```python 
if current.next and current.val == current.next.val:
                val_to_delete = current.val
                continue
```

