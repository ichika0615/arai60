#二重ループの解法
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current is not None:
            while current.next is not None and current.val == current.next.val:
                current.next = current.next.next

            current = current.next
        return head

#2個目のwhileは、current.nextを主眼に置いている。
#current.nextだけをみて繋ぎかえていく。
# while current.val == current.next.val and current.next is not None:
#とかいてerrorを食らう。while　A and B: にも順序があると意識したのは初めて。
    
#time complexity O(n^2) 
#space complexity O(1)


#一重ループを用いた解法
# while ~ conitnueで繰り返すだけ繰り返してcurrent = current.nextで次に向かう
#currentとcurrent.nextを主眼に置いている。
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
                continue
            current = current.next
            #continueで同じ数が連続するだけ繋ぎかえて、次のノード探索。
            
        return head
#time complexiy O(n)
#space complexity O(1)

#while current is not None and... 以下を関数で切り出してみる。
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #現在のノードと次のノードが重複していれば、つなぎ変える
        def is_duplicates(current):
            while current is not None and current.next is not None:
                if current.val == current.next.val:
                    current.next = current.next.next
                    continue
                current = current.next
        
        current = head
        is_duplicates(current)
        return head
#意味ないかも
#長々とした同じような処理が繰り返して続いたら関数でまとめちゃう気持ちかな？



#既存のリンクトリストを変えるのではなく、題意を満たすリンクトリストを新しく作成する。
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #リンクトリストがない時
        if head is None:
            return None
        
        current = head
        new_head = ListNode(head.val)
        #先頭のノード作成(絶対答えに入る)
        new_current = new_head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
                continue
            current = current.next
            new_next_current = ListNode(current.val)
            new_current.next = new_next_current
            new_current = new_next_current
        return new_head
#space O(n)

#リンクトリストを新しく制作する。
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        new_head = ListNode(head.val)
        current = head
        new_current = new_head

        while current is not None:
            while current.next is not None and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
            if current is None:
                return new_head
            #current.next == Noneの時ぬるぽになるのでその対策
            new_node = ListNode(current.val)
            new_current.next = new_node
            new_current = new_node
        return new_head

#Wrong Answer↓
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
                      
            current = current.next
        return head
#continueを書いてない。2回以上つなぎ変える時に対応できない。
