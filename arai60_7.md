# Step1
- 新しく連結リストを作る or 既存の連結リストを改造して所望の連結リストを作る

## 新しく連結リストを作る。
- 連結リストをheadから順に走査して、リストに値を格納する。それを逆から読んで所望の連結リストを作ればよい。
- 先頭のノードも作っていくので、出発点としてdummyを作っておくといい。
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_node_vals = []
        current = head

        while current:
            visited_node_vals.append(current.val)
            current = current.next
        
        visited_node_vals.reverse()
        dummy = ListNode()
        ans_node = dummy

        for val in visited_node_vals:
            ans_node.next = ListNode(val)
            ans_node = ans_node.next 
        
        return dummy.next
```

- T: O(N)/ M: O(N)
- reverse()メソッドは計算量がO(N)。

## stackを使う
- 先ほどと同じように。連結リストを走査して値をスタックに格納し取り出していけば所望の連結リストを得る。
- ちなみに、pop()メソッドの計算量は末尾をpopするならO(1)。l[i]をpopするならO(N-i)。
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_vals = []   #stack
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
- T: O(N)/ M:O(N)

# Step2
- 他の方のコードを見ていく。
## iterative
- 既存の連結リストを改造して所望の連結リストを得る方法(sc:O(1))
- ２つのポインターを用いて、頭からリストの方向を逆にしていく。端に到達したら終了。
- https://www.youtube.com/watch?v=G0_I-ZF0S38&t=253s を見てようやく理解した。
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        return previous
```
- T:O(N)/ M:O(1)

## recursive
- iterativeと発想は同じで、再帰で書く方法もある。
- ノードの数は最大5000より、再帰に使えるスタック深さを変更しておく。
- ただ、LeetCodeではデフォルトで55000回再帰呼び出しできるらしいので、実はいらない。
```python
import sys
sys.setrecursionlimit(10**4)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reversenodes(current, previous):
            #ベースケース
            if current is None:
                return previous
            #currentのノードから伸びる矢印を反対にする
            next_node = current.next
            current.next = previous
            #再帰呼び出し
            return reversenodes(next_node, current)
        
        return reversenodes(head, None)
```
- T:O(N)/ M:O(N)
- 再帰呼び出しでメモリを使う。

## 後ろから順々に作る。
- reversed_headをNone(末尾)で初期化しておいて、先頭から連結リストを走査して後ろに繋げていけば、所望の連結リストを得る。
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        reversed_head = None  

        while current:
            reversed_head = ListNode(val=current.val, next=reversed_head)
            current = current.next
        
        return reversed_head
```
- T:O(N)/ M:O(N)

# Step3
## stackを用いる。
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_vals = []  #stack
        current = head

        while current:
            node_vals.append(current.val)
            current = current.next
        
        dummy = ListNode()
        last_node = dummy

        while node_vals:
            last_node.next = ListNode(val=node_vals.pop())
            last_node = last_node.next
        
        return dummy.next
```
- `while current`と書いたのだから、`while node_vals`として表記を統一した。
- 直感的で一番わかりよい。

## iterative
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        return previous
```

## recursive
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseNodes(current, previous):
            # base case
            if current is None:
                return previous
            
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            #この操作をベースケースに到達するまで繰り返す
            return reverseNodes(current, previous)
        
        return reverseNodes(head, None)
```

# wrong answer
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = ListNode(next=head)

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        return previous
```
- MLE
- テストケースなら、5 -> 4 -> 3 -> 2 -> 1 -> 0 -> 1 -> 0 -> 1 -> 0 -> 1 -> ....
- 似たようなミスを過去もやった。尻尾をNone以外で受けてしまうとそこにサイクルが生じて処理が終わらない。
