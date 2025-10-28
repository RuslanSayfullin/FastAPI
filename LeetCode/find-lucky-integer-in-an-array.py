from typing import List
from collections import Counter

# Для массива целых чисел arr счастливое целое число — это целое число, частота появления которого в массиве равна его значению.
# Верните наибольшее счастливое целое число в массиве. Если счастливого целого числа нет, верните -1.

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_dict = Counter(arr)
        result = -1

        for key, value in arr_dict.items():
            if key == value and key > result:
                result = key
            
        return result


arr = [2,2,3,4]
example = Solution()
result1 = example.findLucky(arr)
print(result1)

arr = [1,2,2,3,3,3]
result2 = example.findLucky(arr)
print(result2)

arr = [2,2,2,3,3]
result3 = example.findLucky(arr)
print(result3)