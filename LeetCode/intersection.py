from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        result = list(set1.intersection(set2))
        return result


nums1 = [1,2,2,1]
nums2 = [2,2]
example1 = Solution()
result1 = example1.intersection(nums1, nums2)
print(result1)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
example2 = Solution()
result2 = example2.intersection(nums1, nums2)
print(result2)