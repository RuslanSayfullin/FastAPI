from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = Counter(nums)
        flag = False
        
        for key in result.values():
            if key > 1:
                flag = True

        return flag

nums = [1,2,3,1]
example1 = Solution()
result1 = example1.containsDuplicate(nums)
print(result1)

nums = [1,2,3,4]
example2 = Solution()
result2 = example2.containsDuplicate(nums)
print(result2)

nums = [1,1,1,3,3,4,3,2,4,2]
example3 = Solution()
result3 = example3.containsDuplicate(nums)
print(result3)

