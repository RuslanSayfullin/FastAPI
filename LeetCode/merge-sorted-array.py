import copy
from typing import List

"""Вам даны два целочисленных массива nums1 и nums2, отсортированные в порядке неубывания, 
и два целых числа m и n, представляющие количество элементов в nums1 и nums2 соответственно.
Объедините nums1 и nums2 в один массив, отсортированный в порядке неубывания.
Функция не должна возвращать итоговый отсортированный массив, а должна хранить его внутри массива nums1. 
Для этого длина nums1 равна m + n, где первые m элементов обозначают элементы, которые должны быть объединены, 
а последние n элементов равны 0 и должны быть проигнорированы. Длина nums2 равна n."""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        arr = copy.deepcopy(nums1)
        l = r = k = 0

        while l < m and r < n:
            if arr[l] < nums2[r]:
                nums1[k] = arr[l]
                l += 1
            else:
                nums1[k] = nums2[r]
                r += 1
            k += 1

        while l < m:
            nums1[k] = arr[l]
            l += 1
            k += 1

        
        while r < n:
            nums1[k] = nums2[r]
            r += 1
            k += 1

            
        

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
example =Solution()
example.merge(nums1, m, nums2, n)
assert nums1 == [1,2,2,3,5,6]
print("example1: ", nums1)

nums1 = [1]
m = 1
nums2 = []
n = 0
example.merge(nums1, m, nums2, n)
assert nums1 == [1]
print("example2: ", nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
example.merge(nums1, m, nums2, n)
assert nums1 == [1]
print("example3: ", nums1)