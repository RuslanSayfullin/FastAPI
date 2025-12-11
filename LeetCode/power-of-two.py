from collections import Counter

"""
Если задано целое число n, верните true, если оно является степенью двойки. В противном случае верните false.
Целое число n является степенью двойки, если существует целое число x такое, что n == 2x.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n >=0:
            bin_n = bin(n)
            data = Counter(bin_n)
            if data.get('1') == 1:
                return True
            else:
                return False
        else:
            return False



n = 1
example =Solution()
result1 = example.isPowerOfTwo(n)
assert result1 == True
print(result1)

n = 16
result2 = example.isPowerOfTwo(n)
assert result2 == True
print(result2)

n = 3
result3 = example.isPowerOfTwo(n)
assert result3 == False
print(result3)