# Step 1
- 初見ではビビるぐらい何もわからなかった。まず解答の形式すらつかめなかった。他の方のコードを見てやっと理解した。
# Step 2

## ソートを用いる
- まず初期状態のリストを降順にソートして、addメソッドが呼びだされるたびに値を追加してまたソートする。k番目をインデクスで指定して取り出す。
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)


    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]
```

## k番目より低い点数はいらないから除外する。addメソッドでは末尾のアイテムを取り出せばそれが答え。
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        if len(self.nums) > self.k:
            self.nums = self.nums[:self.k]

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        if len(self.nums) > self.k:
            self.nums = self.nums[:self.k]
        return self.nums[-1]
```

## 優先度付きキュー(ヒープ)を用いる。
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while self.k < len(self.nums):
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while self.k < len(self.nums):
            heapq.heappop(self.nums)
        return self.nums[0]
```
- heapq.heapify()は破壊的。

### heapifyの代わりにheappushを使用
```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_scores = []  #heap
        for num in nums:
            heapq.heappush(self.top_k_scores, num)
        while self.k < len(self.top_k_scores):
            heapq.heappop(self.top_k_scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.top_k_scores, val)
        while self.k < len(self.top_k_scores):
            heapq.heappop(self.top_k_scores)
        return self.top_k_scores[0]
```
# Step 3
## リストを用いる方法
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        if self.k < len(self.nums):
            self.nums = self.nums[:self.k]

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        if self.k < len(self.nums):
            self.nums = self.nums[:self.k]
        return self.nums[-1]
```
## heapを用いる方法
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_scores = []  #heap
        for num in nums:
            heapq.heappush(self.top_k_scores, num)
        while self.k < len(self.top_k_scores):
            heapq.heappop(self.top_k_scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.top_k_scores, val)
        while self.k < len(self.top_k_scores):
            heapq.heappop(self.top_k_scores)
        return self.top_k_scores[0]
```

## heapifyを使う
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.k = k
        self.top_k_scores = nums
        while self.k < len(self.top_k_scores):
            heapq.heappop(self.top_k_scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.top_k_scores, val)
        while self.k < len(self.top_k_scores):
            heapq.heappop(self.top_k_scores)
        return self.top_k_scores[0]
```
