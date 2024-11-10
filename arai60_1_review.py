class Solution:
    def hasCycle(self, head: Optional[ListNode], visited_nodes = None) -> bool:
        current = head
        if visited_nodes == None:
            visited_nodes = set()
        
        if current in visited_nodes:
            return True
        if current not in visited_nodes:
            visited_nodes.add(current)
        if current == None:
            return False

        current = current.next
        return self.hasCycle(current, visited_nodes)

# 再帰深さ　N
# Pythonはデフォルトで1000回ほど再帰呼び出しできる。
# sys.setrecursionlimit(limit)で調節可能
