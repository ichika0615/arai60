# 全くわからず、答えを見た。
# 連結リストをよく理解していなかった。
# 本質的には、連結リストは値とポインターが格納されたデータの群集であり、それらは散在していてポインターの見えない糸で繋がっている。

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current is not None:
            #current.nextがぬるぽにならないようにwhile~を書くんですよ、と解釈しているが、
            #なんか、current.next is not None が必要な可能性は？と考えてしまう。
            #current.next.nextがどこかのタイミングで出てくるのでは？
            #感覚として、今から、current.next以降を見て、それらがcurrent自分自身と被ってないかをチェック
            #この階層ではcurrent = current.next(次のノードに移動)以外使うわけないよね
            while current.next is not None and current.val == current.next.val: #自分と隣の値が同じなら
                current.next = current.next.next #current.nextを繋ぎ変え続ける作業
            current = current.next
        return head
                
    
