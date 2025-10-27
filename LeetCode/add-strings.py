import sys

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Увеличиваем лимит для больших чисел
        sys.set_int_max_str_digits(10000)
        
        num1_int = int(num1)
        num2_int = int(num2)
        
        return str(num1_int + num2_int)

num1 = "11"
num2 = "123"
example =Solution()
result1 = example.addStrings(num1, num2)
print(result1, print(type(result1)))

num1 = "456"
num2 = "77"
result2 = example.addStrings(num1, num2)
print(result2, print(type(result2)))

num1 = "0"
num2 = "0"
result3 = example.addStrings(num1, num2)
print(result3, print(type(result3)))

num1 = "hello"
num2 = "0"
result4 = example.addStrings(num1, num2)
print(result4)