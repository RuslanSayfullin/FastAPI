
# Операция XOR в массиве
# Дано целое число n и целое число start.
# Определите массив nums, где nums[i] = start + 2 * i (индексация начинается с 0) и n == nums.length.
# Верните результат побитового XOR всех элементов массива nums.

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result

n = 5
start = 0
example = Solution()
result1 = example.xorOperation(n, start)
print(result1)

n = 4
start = 3
result2 = example.xorOperation(n, start)
print(result2)

