#setを用いた解法は安定して解ける。解くときは、３回連続でacされることを確認する。
#解く時に、言語化をするように意識する。

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set() #探索したノードを記録する。
        current = head # 最初はheadから見ていく。

        while current is not None: #current.nextでぬるぽにならない内は……(currentが端に達さない内は)
            if current in visited_nodes: #来たノードが、すでに探索したやつなら
                return current #それが答えだからreturn
            visited_nodes.add(current) #そうじゃないなら、記録する。
            current = current.next #次のノードに移動する。
        return None #currentが端っこに来たなら、循環がないからNone返す。


#フロイドの循環検出を用いる方法も結構紹介されていることだし、一応やる。
#それぞれ、亀と兎が出発してから初めて会う場所(衝突点)から、headから、2人が同じ速さで移動して、両者が出会うところが循環の入り口。
#検証すると確かにそうだけど、まだなんかピンとこない。
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                meeting_node = slow
                start_node = head
                
                while True:
                    meeting_node = meeting_node.next
                    start_node = start_node.next
                    if meeting_node == start_node:
                        return meeting_node
        return None
                    
        
# wrong answer
# while True内部がおかしい。
# [1, 2] pos = 0 の時、衝突点と出発点は同じで、すでに条件を満たしているのに、2人が一緒に隣に移動してそこを出力してしまってる。
# meeting_node = meeting_node.next start_node = start_node.next -> if meeing_node == start_node
#逆
    
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                meeting_node = slow
                start_node = head
                
                while True:
                    if meeting_node == start_node:
                        return meeting_node
                    meeting_node = meeting_node.next
                    start_node = start_node.next
        
        return None
#AC
#むっずー
#他の方の解法を見ると、関数の再帰を用いて解いている方もいて、色々な開放があるとわかった。
#やはり色々な解法で書けるようになることは重要なのでしょうか？
    
