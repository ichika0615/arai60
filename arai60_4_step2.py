class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        each_node_nums = {} 
        #key: values of nodes 
        #vals: frequence

        current = head
        while current:
            each_node_nums[current.val] = 1 + each_node_nums.get(current.val, 0)
            current = current.next
        
        sentinel = ListNode()
        new_prev = sentinel
        for node, freq in each_node_nums.items():
            if freq == 1:
                new_node = ListNode(val=node, next=None)
                new_prev.next = new_node
                new_prev = new_node
        return sentinel.next
    #new_prevの命名に不安がある。
    #new_prevは、自分で作ったリンクトリスト要素を繋いでいくのに使う。
    #新しい要素を作ったら後ろのやつと繋げる必要があり、一個前のやつを持っておく必要があるから。
  
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        dummy = ListNode()
        last_distinct_node = dummy
        
        # while current: とか, if current.next　とかのスコープ？に気をつけろ。
        while current:
            if current.next and current.val == current.next.val:
                #ここではcurrentの更新がないから、一番はじめのwhile current:の条件が効いてる。↑
                deleting_val = current.val
                while current and current.val == deleting_val:
                    #currentが更新されるループ。whileにcurrentが存在していることを条件としてかけ。
                    current = current.next
                continue
            new_node = ListNode(current.val)
            last_distinct_node.next = new_node
            last_distinct_node = new_node
            current = current.next
        last_distinct_node.next = None
        return dummy.next
    
#Wrong answer ↓
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        dummy = ListNode()
        last_distinct_node = dummy

        while current:
            if current.next and current.val == current.next.val:
                deleting_val = current.val
                while current.val == deleting_val:
                    current = current.next
                    # AttributeError current == Noneになってた
                continue
            last_distinct_node.next = current
            last_distinct_node = current
            current = current.next
        last_distinct_node.next = None
        return dummy.next          

