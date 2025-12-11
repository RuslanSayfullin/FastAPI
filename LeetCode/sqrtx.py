"""
Дано неотрицательное целое число x. Верните квадратный корень из x, округленный до ближайшего целого числа в меньшую сторону. 
Возвращаемое целое число также должно быть неотрицательным.
Не используйте встроенные функции или операторы возведения в степень.
Например, не используйте pow(x, 0.5) в C++ или x ** 0.5 в Python.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        
        min_bound = 0
        if x > 0:
            for i in range(x+1):
                
                if i * i <= x:
                    min_bound = i
                else:
                    return min_bound
         
        return min_bound

x = 1
example =Solution()
result1 = example.mySqrt(x)
#assert result1 == 2
print(result1)

"""
x = 8
result2 = example.mySqrt(x)
assert result2 == 2
print(result2)
"""
