"""Напишите алгоритм для определения, является ли число n счастливым.
Счастливое число — это число, определяемое следующим образом:
    Начиная с любого положительного целого числа, замените число суммой квадратов его цифр.

    Повторяйте процесс, пока число не станет равным 1 (где оно и останется), или пока цикл не зациклится до бесконечности, не включая 1.
Т   е числа, для которых этот процесс заканчивается на 1, являются счастливыми.

Возвращайте true, если n — счастливое число, и false в противном случае."""

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total += digit ** 2
            return total
        
        slow = n
        fast = get_next(n)
        
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return fast == 1


n = 19
example = Solution()
result1 = example.isHappy(n)
print(result1)

n = 2
result2 = example.isHappy(n)
print(result2)
