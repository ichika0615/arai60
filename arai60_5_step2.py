# 他の方のコードを見ていく。

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_val(node):
            #ノードの数字何かな？あ、5。or え、ないやん、０。
            if node is None:
                return 0
            return node.val

        current_1 = l1
        current_2 = l2
        dummy = ListNode()
        list_designer = dummy
        carry = 0

        while current_1 or current_2 or carry:
            total = get_val(current_1) + get_val(current_2) + carry
            new_node = ListNode(val=total%10)
            list_designer.next = new_node
            list_designer = new_node
            carry = total // 10

            if current_1:
                current_1 = current_1.next
            if current_2:
                current_2 = current_2.next
        
        return dummy.next

#再帰
#再帰の深さは最大100。
#Pythonのスタック深さの最大値はleetcodeでは550000。print(sys.getrecursionlimit())で確認できる。
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_val(node):
            if node is None:
                return 0
            return node.val
        
        def next_node(node):
            if node is None:
                return None
            return node.next
        
        #再帰関数
        def add_two_nums(current_1, current_2, carry):
            if not (current_1 or current_2 or carry):
                return None

            total = get_val(current_1) + get_val(current_2) + carry
            new_node = ListNode(val=total%10)
            carry = total // 10
            new_node.next = add_two_nums(next_node(current_1), next_node(current_2), carry)
            return new_node
        
        return add_two_nums(l1, l2, 0)


#current_1, 2　とかするのめんどくさいなら、l1、l2のまま動かしていい。
#三項演算子は、これくらい短いなら使ってもいいかな。
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        list_designer = dummy
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry
            new_node = ListNode(val=total % 10)
            list_designer.next = new_node
            list_designer = new_node
            carry = total // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next 










