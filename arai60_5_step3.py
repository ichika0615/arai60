#　一番好き。
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_val(node):
            if node is None:
                return 0
            return node.val
        
        current_1 = l1
        current_2 = l2
        carry = 0
        dummy = ListNode()
        list_designer = dummy

        while current_1 or current_2 or carry:

            total = get_val(current_1) + get_val(current_2) + carry
            node = ListNode(total%10)
            list_designer.next = node
            list_designer = node
            carry = total // 10
            
            if current_1:
                current_1 = current_1.next
            if current_2:
                current_2 = current_2.next
        
        return dummy.next
  
#１つも関数使わなかったらめちゃくちゃ長ったらしくなる。
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_1 = l1
        current_2 = l2
        carry = 0
        dummy = ListNode()
        list_designer = dummy

        while current_1 or current_2 or carry:
            if current_1 and current_2:
                total = current_1.val + current_2.val + carry
                node = ListNode(total%10)
                list_designer.next = node
                list_designer = node
                carry = total // 10
            elif current_1:
                total = current_1.val + carry
                node = ListNode(total%10)
                list_designer.next = node
                list_designer = node
                carry = total // 10
            elif current_2:
                total = current_2.val + carry
                node = ListNode(total%10)
                list_designer.next = node
                list_designer = node
                carry = total // 10
            else:
                total = carry
                node = ListNode(total%10)
                list_designer.next = node
                list_designer = node
                carry = total // 10
            
            if current_1:
                current_1 = current_1.next
            if current_2:
                current_2 = current_2.next

        return dummy.next


#再帰
#深さは連結リストのノード数の多い方(+1)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_val(node):
            if node is None:
                return 0
            return node.val

        def add_numbers(l1, l2, carry):
            if not(l1 or l2 or carry):
                return None
            total = get_val(l1) + get_val(l2) + carry
            node = ListNode(val=total%10)
            carry = total // 10
            
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
            node.next = add_numbers(l1, l2, carry)
            return node
        
        return add_numbers(l1, l2, 0)
            




        