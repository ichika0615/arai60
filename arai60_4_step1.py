# 方針
# ハッシュテーブルにノードの数字とその数を記録して、数が一個(distinct)のものだけを
# 拾い上げて、題意を満たすリンクトリストを新しく作る。
#concat.filter.group?
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        each_node_nums = {} 
        #key:value of node 
        #val: how often this value occures
        current = head

        while current:
            each_node_nums[current.val] = 1 + each_node_nums.get(current.val, 0)
            current = current.next
        
        dummy = ListNode(val=-1000)
        new_current = dummy

        for node_val, num in each_node_nums.items():
            if num == 1:
                new_node = ListNode(val=node_val)
                new_current.next = new_node
                new_current = new_node
        return dummy.next
#time complexity O(N+K) K:ノードの番号の種類の数
#space complexity O(N)

#リンクトリストをつなぎ直して所望のリンクトリストを作る
# last_unique_node: distinctなリンクトリストの最後のノード(暫定)
# currentでノードを見ていき、distinctと分かったら、それが所望のlinked listの暫定最終ノード
# last_unique_nodeがノードを走査して繋いでいく。
    
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        last_distinct_node = dummy
        current = head

        while current:
            if current.next and current.val == current.next.val:
                #この番号のノードは全部消す。
                deleting_num = current.val
                while current and current.val == deleting_num:
                    current = current.next
                continue

            last_distinct_node.next = current
            last_distinct_node = current
            current = current.next
        last_distinct_node.next = None
        return dummy.next


#wrong answers ↓
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        last_distinct_node = dummy
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next
                #ぺけ。current.val != current.next.valで処理が止まる
                continue

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        last_distinct_node = dummy
        current = head

        while current and current.next:
            # だめ。最後のノードが考慮されない。
            # 第３問はなんでwhile current and current.next: でいけたんだっけ。
            if current.val == current.next.val:
                #この番号のノードは全部消す。
                deleting_num = current.val
                while current and current.val == deleting_num:
                    current = current.next
                continue

            last_distinct_node.next = current
            last_distinct_node = current
            current = current.next
        last_distinct_node.next = None
        return dummy.next




            





