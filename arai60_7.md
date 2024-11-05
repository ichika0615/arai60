# Step1
- 新しく連結リストを作る or 既存の連結リストを改造して所望の連結リストを作る

- 新しく連結リストを作る。
- 連結リストをheadから順に走査して、リストに値を格納する。それを逆から読んで所望の連結リストを作ればよい。
- 先頭のノードも作っていくので、出発点としてdummyを作っておくといい。
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_vals = []
        current = head

        while current:
            node_vals.append(current.val)
            current = current.next
        
        dummy = ListNode()
        reversed_list = dummy

        node_vals.reverse()
        for val in node_vals:
            node = ListNode(val)
            reversed_list.next = node
            reversed_list = node
        
        return dummy.next
```
- tc: O(N)   sc: O(N)
- reverse()メソッドは計算量がO(N)。

- stackを使ってやってみる
- 先ほどと同じように。連結リストを走査して値をスタックに格納し取り出していけば所望の連結リストを得る。
- ちなみに、pop()メソッドの計算量は末尾をpopするならO(1)。l[i]をpopするならO(N-i)。

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_vals = [] #stack
        current = head
        
        while current:
            node_vals.append(current.val)
            current = current.next
        
        dummy = ListNode()
        reversed_list= dummy

        while node_vals != []:
            node = ListNode(node_vals.pop())
            reversed_list.next = node
            reversed_list = node
        
        return dummy.next
```
- tc: O(N)  sc:O(N)

# Step2
- 他の方のコードを見ていく。
- 既存の連結リストを改造して所望の連結リストを得る方法(sc:O(1))





      
