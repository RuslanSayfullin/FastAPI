from typing import List

# Разделение массива
# Дан массив целых чисел nums из 2n целых чисел. Сгруппируйте эти числа в n пар (a1, b1), (a2, b2), ..., (an, bn) так, чтобы сумма min(ai, bi) для всех i была максимальной. 
# Верните максимальную сумму.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Сортируем массив
        nums.sort()

        # Суммируем каждый второй 
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        
        return result

        

nums = [1,4,3,2]
example = Solution()
result1 = example.arrayPairSum(nums)
print(result1)

nums = [6,2,6,5,1,2]
result2 = example.arrayPairSum(nums)
print(result2)

