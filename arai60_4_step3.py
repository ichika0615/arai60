class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        each_node_nums = {}
        current = head

        while current:
            each_node_nums[current.val] = 1 + each_node_nums.get(current.val, 0)
            current = current.next
        
        dummy = ListNode()
        new_prev = dummy
        for node_val, freq in each_node_nums.items():
            if freq == 1:
                new_node = ListNode(node_val)
                new_prev.next = new_node
                new_prev = new_node
        return dummy.next

#time complexity O(N+K)
#space complexity O(N)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        dummy = ListNode()
        list_designer = dummy

        while current:
            if current.next and current.val == current.next.val:
                deleting_val = current.val

                while current and current.val == deleting_val:
                    current = current.next
                continue
            
            list_designer.next = current
            list_designer = current
            current = current.next

        list_designer.next = None
        return dummy.next
# 一番綺麗に見える
# 所望のリストを構成していく変数に見えるので、list_designerとした。


  