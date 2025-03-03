# Step 1
## 先頭からsを走査して、open bracketsは順にスタックに積み込んで、close bracketsが現れるごとにスタックからpopする。出てくるのが対応するopen bracketsであって最終的にスタックが空になっていればTrue
```python
class Solution:
    def isValid(self, s: str) -> bool:
        def is_appropriate(el):
            return el == '(' or el == '{' or el == '[' or el == ')' or el == '}' or el ==']'

        found_open_brackets = []  #This is a stack.
        for s_item in s:
            if not is_appropriate(s_item):
                raise ValueError('inappropriate input')
            if s_item == '(':
                found_open_brackets.append(s_item)
            if s_item == '{':
                found_open_brackets.append(s_item)
            if s_item == '[':
                found_open_brackets.append(s_item)
            if s_item == ')':
                if not found_open_brackets:
                    return False
                open_bracket = found_open_brackets.pop()
                if open_bracket != '(':
                    return False
            if s_item == '}':
                if not found_open_brackets:
                    return False
                open_bracket = found_open_brackets.pop()
                if open_bracket != '{':
                    return False
            if s_item == ']':
                if not found_open_brackets:
                    return False
                open_bracket = found_open_brackets.pop()
                if open_bracket != '[':
                    return False
        
        if not found_open_brackets:
            return True
        else:
            return False  
```
- 時間計算量: O(N) 空間計算量: O(N)


# Step 2
- Step1ではカッコの種類が3種類だから書けているが、入力の種類が増えるとえらいことになる。他の方のコードを見ると、ハッシュマップに開きと閉じの対応を保存していて賢いと思った。
```python
class Solution:
    def isValid(self, s: str) -> bool:
        OPEN_BRACKETS = '({['
        CLOSED_BRACKETS = ')}]'
        OPEN_TO_CLOSED = {'(': ')', '{': '}', '[': ']'}

        def is_appropriate(el):
            return el in OPEN_BRACKETS or el in CLOSED_BRACKETS
        
        for bracket in s:
            if not is_appropriate(bracket):
                raise ValueError('inappropriate input')
            
        found_open_brackets = []  # This is a stack.
        for bracket in s:
            if bracket in OPEN_BRACKETS:
                found_open_brackets.append(bracket)
            if bracket in CLOSED_BRACKETS:
                if not found_open_brackets:
                    return False
                open_bracket = found_open_brackets.pop()
                if bracket != OPEN_TO_CLOSED[open_bracket]:
                    return False
        if not found_open_brackets:
            return True
        else:
            return False 
```

- dequeを使っている人もいた。今回はstackなので右側のpopとappendしか登場せずいうほど高速化されるかな、という気持ちもある。
```python
class Solution:
    def isValid(self, s: str) -> bool:
        OPEN_BRACKETS = '({['
        CLOSED_BRACKETS = ')}]'
        OPEN_TO_CLOSED = {'(': ')', '{': '}', '[': ']'}
        
        found_open_brackets = deque()  # This is a stack.
        for bracket in s:
            if bracket not in OPEN_BRACKETS and bracket not in CLOSED_BRACKETS:
                continue
            if bracket in OPEN_BRACKETS:
                found_open_brackets.append(bracket)
            if bracket in CLOSED_BRACKETS:
                if not found_open_brackets:
                    return False
                open_bracket = found_open_brackets.pop()
                if bracket != OPEN_TO_CLOSED[open_bracket]:
                    return False
        
        if not found_open_brackets:
            return True
        else:
            return False
```

# Step 3
```python
class Solution:
    def isValid(self, s: str) -> bool:
        OPEN_BRAKCETS = ('(', '{', '[')
        CLOSED_BRAKCETS = (')', '}', ']')
        OPEN_TO_CLOSED = {'(': ')', '{': '}', '[': ']'}
        
        found_open_brackets = []  # This is a stack.
        for bracket in s:
            if bracket in OPEN_BRAKCETS:
                found_open_brackets.append(bracket)
            elif bracket in CLOSED_BRAKCETS:
                if not found_open_brackets:
                    return False
                open_bracket = found_open_brackets.pop()
                if bracket != OPEN_TO_CLOSED[open_bracket]:
                    return False
        
        return not found_open_brackets
```
- 自由文脈文法やチョムスキー階層、プッシュダウンオートマトンが連想されるらしい。オートマトンや計算機については絶賛勉強中。わかったら下にちゃんとまとめたい。


