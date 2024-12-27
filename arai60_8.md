# Step 1
- 解答の形式を掴むのが難しかった。他の方のコードを見てちゃんと理解した。
# Step 2

## ソートを用いる。リストに点数を格納して、新しいスコアが追加されたらいちいちソートする。
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
- 時間計算量: __init__ O(nlogn)  add O(nlogn)
- 空間計算量: O(n)

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
- 時間計算量: __init__ O(nlogn)  add O(nlogn)
- 空間計算量: O(n)

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
- 時間計算量: __init__ O(nlogn)  add O(logn)
- 空間計算量: O(n)


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
- 時間計算量: __init__ O(nlogn)  add O(logn)
- 空間計算量: O(n)

# Step 3
## リストを用いる方法
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_scores = nums
        self.top_k_scores.sort(reverse=True)
        if k < len(self.top_k_scores):
            self.top_k_scores = self.top_k_scores[:k]


    def add(self, val: int) -> int:
        self.top_k_scores.append(val)
        self.top_k_scores.sort(reverse=True)
        if self.k < len(self.top_k_scores):
            self.top_k_scores = self.top_k_scores[:self.k]
        return self.top_k_scores[-1]
```
- 時間計算量: __init__ O(nlogn)  add O(logn)
- 空間計算量: O(n)

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
        self.k = k
        heapq.heapify(nums)
        self.top_k_scores = nums  # heap
        while self.k < len(self.top_k_scores):
            heapq.heappop(self.top_k_scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.top_k_scores, val)
        while self.k < len(self.top_k_scores):
            heapq.heappop(self.top_k_scores)
        return self.top_k_scores[0]
```
heap実装が難しくてできなかった。よく考えてやってみます。できたらまたアップします。


## 無理やりクイックセレクト
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
       self.k = k
       self.top_k_scores = []
       for num in nums:
        self.top_k_scores.append(num)

    def quick_select(self, left, right):
        pivot_index = random.randint(left, right)
        pivot = self.top_k_scores[pivot_index]
        self.top_k_scores[pivot_index] , self.top_k_scores[right] = self.top_k_scores[right], self.top_k_scores[pivot_index]

        partition_index = left
        for i in range(left, right):
            if self.top_k_scores[i] > pivot:
                self.top_k_scores[i], self.top_k_scores[partition_index] = self.top_k_scores[partition_index], self.top_k_scores[i]
                partition_index += 1
        
        self.top_k_scores[partition_index], self.top_k_scores[right] = self.top_k_scores[right], self.top_k_scores[partition_index]

        if partition_index == self.k - 1:
            return None
        elif partition_index < self.k - 1:
            return self.quick_select(partition_index + 1, right)
        elif partition_index > self.k - 1:
            return self.quick_select(left, partition_index - 1)

    def add(self, val: int) -> int:
        self.top_k_scores.append(val)
        self.quick_select(0, len(self.top_k_scores)-1)
        return self.top_k_scores[self.k - 1]
```
- 時間計算量: __init__ O(n)  quick_select: O(n)(最悪計算量: O(n^2))  add O(n)
- 空間計算量: O(n)

まぁ想定解ではないでしょう。
