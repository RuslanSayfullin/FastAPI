from typing import List
from collections import Counter


"""Дан целочисленный массив размером n. Найдите все элементы, которые встречаются более ⌊ n/3 ⌋ раз."""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        if len(nums) < 1:
            return []
        else:
            result = []
            threshold = len(nums) / 3

            main_dict = Counter(nums)
            for key, value in main_dict.items():
                if value > (threshold):
                    result.append(key)

            return result




nums = [3,2,3]
example =Solution()
result1 = example.majorityElement(nums)
assert result1 == [3]
print(result1)

nums2 = [1]
result2 = example.majorityElement(nums2)
assert result2 == [1]
print(result2)

nums3 = [1,2]
result3 = example.majorityElement(nums3)
assert result3 == [1,2]
print(result3)