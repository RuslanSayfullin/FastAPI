class Solution:
    def isPalindrome(self, x: int) -> bool:
        if not isinstance(x, int) or x < 0:
            print(f"{x} is not palindrom")
            return False

        original_number = x
        reversed_number = 0

        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x = x // 10
            print(digit, reversed_number, x)

        if original_number == reversed_number:
            print(f"{original_number} is palindrom")
            return True
        else:
            print(f"{original_number} is not palindrom")
            return False

        

example = Solution()

numbers = [121, -121, 567, 565, "111"]
for i in numbers:
    print(example.isPalindrome(i))

