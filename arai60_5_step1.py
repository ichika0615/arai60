# 数字を読み取って、足して、また連結リストにもどす
# 直感的だが効率悪そう。
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_1 = 0
        number_2 = 0

        current_1 = l1
        current_2 = l2

        place = 1
        while current_1:
        
            number_1 += current_1.val * place
            place *= 10
            current_1 = current_1.next
        place = 1
        while current_2:
            
            number_2 += current_2.val * place
            place *= 10
            current_2 = current_2.next
        
        ans = number_1 + number_2
        

        ans_list = [int(x) for x in list(str(ans))]

        ans_head = ListNode(val=ans%10)
        current = ans_head

        for i in range(len(ans_list)-2, -1, -1):
            new_node = ListNode(val=ans_list[i])
            current.next = new_node
            current = new_node
        
        return ans_head

#連結リストのまま足していく。
  
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_1 = l1
        current_2 = l2
        dummy = ListNode()
        list_designer = dummy
        add_next = 0

        while current_1 or current_2:
            if current_1 and current_2:
                node_sum = current_1.val + current_2.val + add_next
                new_node = ListNode(val=node_sum%10)
                list_designer.next = new_node
                list_designer = new_node
                add_next = node_sum//10
                current_1 = current_1.next
                current_2 = current_2.next

            elif current_1:
                node_sum = current_1.val + add_next
                new_node = ListNode(val=node_sum%10)
                list_designer.next = new_node
                list_designer = new_node
                add_next = node_sum//10
                current_1 = current_1.next

            else:
                node_sum = current_2.val + add_next
                new_node = ListNode(val=node_sum%10)
                list_designer.next = new_node
                list_designer = new_node
                add_next = node_sum//10
                current_2 = current_2.next
            
        if add_next != 0:
            list_designer.next = ListNode(val=add_next)
            #一回バーっとコード書いた時は忘れてた。whileにcarryも入れておけばもっとスムーズ

        return dummy.next

# 関数で切り出そうとしたら失敗した。
# UnboundLocalError: cannot access local variable 'list_designer' where it is not associated with a value
# 変数のスコープも何も考えてなかった。
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # initialized the variables here

        def designList(node_sum):
            new_node = ListNode(val=node_sum%10)
            list_designer.next = new_node
            list_designer = new_node

        while current_1 or current_2:
            if current_1 and current_2:
                node_sum = current_1.val + current_2.val + add_next
                designList(node_sum)
                add_next = node_sum//10
                current_1 = current_1.next
                current_2 = current_2.next
                #以下略
