from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write_index = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                print(nums[write_index] ,nums[i])
                nums[write_index] = nums[i]
                print(nums)

                write_index += 1
        
        # Дополнительно: заполнить оставшуюся часть (не обязательно по условию)
        for i in range(write_index, len(nums)):
            nums[i] = "_"  # или любое другое значение
        
        return write_index





example = Solution()

#nums = [1,1,2]
#result = example.removeDuplicates(nums)
#print(result, nums)

nums = [0,0,1,1,1,2,2,3,3,4]
result2 = example.removeDuplicates(nums)
print(result2, nums)

    
