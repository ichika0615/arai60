# 先頭からsを走査して、open bracketsは順にスタックに積み込んで、close bracketsが現れるごとにスタックからpopする。出てくるのが対応するopen bracketsであって最終的にスタックが空になっていればTrue
```python
class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        for s_item in s:
            if s_item == '(':
                open_brackets.append('(')
            elif s_item == '[':
                open_brackets.append('[')
            elif s_item == '{':
                open_brackets.append('{')
            elif s_item == ')':
                if open_brackets == []:
                    return False
                popped_item = open_brackets.pop()
                if popped_item != '(':
                    return False
            elif s_item == ']':
                if open_brackets == []:
                    return False
                popped_item = open_brackets.pop()
                if popped_item != '[':
                    return False
            elif s_item == '}':
                if open_brackets == []:
                    return False
                popped_item = open_brackets.pop()
                if popped_item != '{':
                    return False
        if open_brackets == []:
            return True
        else:
            return False
```
                

