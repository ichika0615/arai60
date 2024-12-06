# Step1
- いろいろ考えたが思いつかなかった。逆にヒープをどう使うかとも考えたが、タプルをヒープに入れる発想がなかった。
# Step2 
####
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values_frequency = {}

        for num in nums:
            if num in values_frequency:
                values_frequency[num] += 1
            else:
                values_frequency[num] = 1
        
        frequent_values = []  #heap
        for value, frequency in values_frequency.items():
            heapq.heappush(frequent_values, (frequency, value))
        
        while k < len(frequent_values):
            heapq.heappop(frequent_values)
        
        return [value for _, value in frequent_values]
```
- 時間計算量:O(N)　空間計算量:O(N)
- N: numsの要素数

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value_to_frequency = {}

        for num in nums:
            value_to_frequency[num] = 1 + value_to_frequency.get(num, 0)
        
        frequency_values = []
        for value, frequency in value_to_frequency.items():
            frequency_values.append([value, frequency])
        
        def get_frequency(item):
            return item[1]
        
        sorted_frequency_values = sorted(frequency_values, key=get_frequency, reverse=True)

        while k < len(sorted_frequency_values):
            sorted_frequency_values.pop()
        
        return [item[0] for item in sorted_frequency_values]

```
- 時間計算量:O(NlogN)　空間計算量:O(N)
- N: numsの要素数

### バケットソート
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values_to_frequency = collections.Counter(nums)
        frequency_values = [[] for _ in range(len(nums)+1)]  #frequency[i]: numbers which occur i times
        for value, frequency in values_to_frequency.items():
            frequency_values[frequency].append(value)
        
        count = 0
        k_frequent_values = []
        for i in range(len(frequency_values)-1, -1, -1):
            if frequency_values[i]:
                k_frequent_values.extend(frequency_values[i])
                count += len(frequency_values[i])
            if count == k:
                break
        
        return k_frequent_values
```
- 時間計算量:O(N)　空間計算量:O(N)
- N: numsの要素数

### コードを整理して見やすくする。
#### 値と頻度をタプルとしてリストに格納して、頻度順でソートする。先頭からk個値を出力する。
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values_to_frequency = {}
        for num in nums:
            values_to_frequency[num] = 1 + values_to_frequency.get(num, 0)
        
        most_frequent_values = []
        for value, frequency in values_to_frequency.items():
            most_frequent_values.append((value, frequency))
        
        most_frequent_values.sort(reverse=True, key=operator.itemgetter(1))

        if k < len(most_frequent_values):
            most_frequent_values = most_frequent_values[:k]
        
        return [value for value, _ in most_frequent_values]
```
- operatorライブラリの確認
- https://docs.python.org/ja/3/library/operator.html
- 機能が結構多いが、主なものは後で手で実装しておく。

#### ヒープを使う。ヒープに値と頻度のタプルを入れていき、k個になるまでpopして値を出力。
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values_to_frequency = {}
        for num in nums:
            values_to_frequency[num] = 1 + values_to_frequency.get(num, 0)
        
        frequenct_values = []  # heap
        for value, frequency in values_to_frequency.items():
            heapq.heappush(frequenct_values, (frequency, value))
        
        while k < len(frequenct_values):
            heapq.heappop(frequenct_values)
        
        return [value for _, value in frequenct_values]
```
####　バケットソート
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values_to_frequency = collections.Counter(nums)

        frequency_values_bucket = [[] for _ in range(len(nums)+1)]  
        #frequency_values_bucket[i]: numbers occuring i times
        for value, frequency in values_to_frequency.items():
            frequency_values_bucket[frequency].append(value)
        
        top_k_values = []
        for i in range(len(frequency_values_bucket)-1, -1, -1):
            if frequency_values_bucket[i]:
                top_k_values.extend(frequency_values_bucket[i])
            if len(top_k_values) == k:
                return top_k_values
            if len(top_k_values) > k:
                return top_k_values[:k]
```
- 制約条件によると答えは一意に定まるが、そうでない場合も一応。
- メモリーをかなり無駄使いしている
#### 辞書を直接ソートする。
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unsorted_values_to_frequency = collections.Counter(nums)
        values_to_frequency = sorted(unsorted_values_to_frequency.items(), reverse= True, key=lambda x:x[1])

        top_k_values = []
        for value, _ in values_to_frequency:
            top_k_values.append(value)
            if len(top_k_values) == k:
                return top_k_values
            if len(top_k_values) > k:
                return top_k_values[:k]
```

# Step3
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values_to_frequency = {}
        for num in nums:
            values_to_frequency[num] = 1 + values_to_frequency.get(num, 0)
        
        frequent_values = []
        for value, frequency in values_to_frequency.items():
            frequent_values.append((value, frequency))
        frequent_values.sort(reverse=True, key=operator.itemgetter(1))

        if k < len(frequent_values):
            frequent_values = frequent_values[:k]
        
        return [value for value, _ in frequent_values]
```

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values_to_frequency = {}
        for num in nums:
            values_to_frequency[num] = 1 + values_to_frequency.get(num, 0)
        
        frequent_values = []  #min-heap
        for value, frequency in values_to_frequency.items():
            heapq.heappush(frequent_values, (frequency, value))
        
        while k < len(frequent_values):
            heapq.heappop(frequent_values)
        
        return [value for _, value in frequent_values]
```
