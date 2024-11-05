# 方針
# ハッシュテーブルにノードの数字とその数を記録して、数が一個(distinct)のものだけを
# 拾い上げて、題意を満たすリンクトリストを新しく作る。
#concat.filter.group?
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], visited_nodes=None) -> Optional[ListNode]:
        visited_nodes = {}
        current = head

        while current:
            visited_nodes[current.val] = 1 + visited_nodes.get(current.val, 0)
            current = current.next
        
        dummy = ListNode()
        distinct_list = dummy
        for node_val, frequency in visited_nodes.items():
            if frequency == 1:
                distinct_list.next = ListNode(node_val)
                distinct_list = distinct_list.next
        
        return dummy.next
#time complexity O(N+K) K:ノードの番号の種類の数
#space complexity O(N)

#連結リストをつなぎ直して所望の連結リストを作る
# last_unique_node: distinctな連結リストの最後のノード(暫定)
# currentでノードを見ていき、distinctと分かったら、それが所望の連結リストの暫定最終ノード
# last_unique_nodeがノードを走査して繋いでいく。
    
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], visited_nodes=None) -> Optional[ListNode]:
        dummy = ListNode()
        distinct_list = dummy
        current = head

        while current:
            if current.next and current.val == current.next.val:
                deleting_val = current.val
                while current and current.val == deleting_val:
                    current = current.next
                continue
            distinct_list.next = current
            distinct_list = distinct_list.next
            current = current.next

        distinct_list.next = None
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




            





