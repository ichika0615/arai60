- 自明な変形を意識する。
## 1
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        
        return head
```
## 2
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
- current.nextの存在はどこで判定されるか？くらいか。

## 3 
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
- 1と何が違う？
- ああ、1は1段目で離脱して、2は2段目で離脱するのか.

## 4 
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current:
            if current.next and current.val == current.next.val:
                current.next = current.next.next
                continue
            current = current.next
        
        return head
```
## 5
- queueで実装する

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        found_vals = [] #queue
        current = head

        while current:
            if current.val not in found_vals:
                found_vals.append(current.val)
            current = current.next
        
        dummy = ListNode()
        distinct_node = dummy

        for val in found_vals:
            distinct_node.next = ListNode(val=val)
            distinct_node = distinct_node.next
        
        return dummy.next
```
- queueじゃないかもw

## 6
- 『一般に、コードを読むのは、ワーキングメモリーを使う行為です。
変数の意味であったり、何が入っていて、どういう処理がなされて、その時点で、どういう値が入る可能性があって、この関数は、例外を投げる可能性があるんだっけないんだっけ。そういうことを考えながら頭の中で走らせています。だから、ワーキングメモリーをさっさと開放してあげることが大事です。』
- 『skip_until_value_change でくくると言いたいことが分かります。
もう一つ、これは current_value のことを忘れてもいいのだということが分かるという意味もあります。』

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def skip_until_value_changes(current_node) -> Optional[ListNode]:
            if current_node.next and current_node.val == current_node.next.val:
                val_to_delete = current_node.val
                while current_node and current_node.val == val_to_delete:
                    current_node = current_node.next
            return current_node
        
        current = head
        
        while current:
            if current.next and current.val == current.next.val:
                current.next = skip_until_value_changes(current)
            current = current.next
        
        return head
```
