# Step1
- いろいろ考えたが思いつかなかった。逆にヒープをどう使うかとも考えたが、タプルをヒープに入れる発想がなかった。
# Step2 
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

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value_to_frequency = {}

        for num in nums:
            value_to_frequency[num] = 1 + value_to_frequency.get(num, 0)
        
        frequency_to_value = [[] for _ in range(len(nums)+1)]  #bucket

        for value, frequency in value_to_frequency.items():
            frequency_to_value[frequency].append(value)
        
        top_k_values = []

        for i in range(len(frequency_to_value)-1, -1, -1):
            if frequency_to_value[i]:
                top_k_values.extend(frequency_to_value[i])
            if len(top_k_values) >= k:
                return top_k_values[:k]
```

