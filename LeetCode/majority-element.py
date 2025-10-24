from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_len = len(nums) / 2
        elements = Counter(nums)

        for key, value in elements.items():
            if value > majority_len:
                return key

nums = [3,2,3]
example =Solution()
result1 = example.majorityElement(nums)
print(result1)

nums = [2,2,1,1,1,2,2]
result2 = example.majorityElement(nums)
print(result2)