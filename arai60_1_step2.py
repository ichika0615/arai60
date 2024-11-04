#hashsetを使う方法はstep2省略

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = (fast.next).next
            if slow == fast:
                return True
        return False

# slow != None は少しまずく、slow is not None　の方が良いらしい。
    
# if slow is fast:　と書いている人がいた。
# == は内容が同じならTrue、isは同一であればTrueを返す。同一性はid()で調べられる。(id:格納されているメモリ上のアドレスを返す)
# 今回は、slowとfastに同じノードが格納されていればreturn Trueして欲しいので、確かにisでも機能する。

# if fast and fast.next: の解釈が難しい。
# fastは2ます動く。その時に、whileの制約をすり抜けて中でNone.nextみたいなのが出たら困るからfast.nextをwhileに入れる。
# 感覚としては、「足の速い猪突猛進fastくんが壁にぶち当たって動けなかったら困るので、whileをすり抜けた以上は走りきれることを保証してあげてね」くらいか。
# 