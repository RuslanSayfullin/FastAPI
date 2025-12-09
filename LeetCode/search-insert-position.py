from typing import List

"""Дан отсортированный массив различных целых чисел и искомое значение. 
Вернуть индекс, если искомое значение найдено. 
Если нет, вернуть индекс, на котором оно было бы, если бы оно было вставлено по порядку.
Вам необходимо написать алгоритм со сложностью выполнения O(log n).
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums = sorted(nums)
            return nums.index(target)


nums = [1,3,5,6]
target = 5

example = Solution()
output1 = example.searchInsert(nums, target)
assert output1 == 2
print(output1)

nums = [1,3,5,6]
target = 2
output2 = example.searchInsert(nums, target)
assert output2 == 1
print(output2)

nums = [1,3,5,6]
target = 7
output3 = example.searchInsert(nums, target)
assert output3 == 4
print(output3)