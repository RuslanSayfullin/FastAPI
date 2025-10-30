"""Строка s считается хорошей, если каждая буква алфавита, содержащаяся в s, встречается как в верхнем, так и в нижнем регистре. 
    Например, «abABB» считается хорошей, потому что в ней встречаются «A» и «a», а также «B» и «b». 
    Однако «abA» не считается хорошей, потому что в ней встречается «b», а «B» — нет.
    Для строки s вернуть самую длинную подстроку строки s, которая является хорошей. 
    Если таких подстроок несколько, вернуть подстроку с самым ранним вхождением. Если их нет, вернуть пустую строку."""


class Solution:
    
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) <2:
            return ""
        
         # Находим буквы, которые нарушают условие "красивости"
        char_set = set(s)


        for i, char in enumerate(s):
            # Если для текущей буквы нет пары (верхний/нижний регистр)
            if char.swapcase() not in char_set:

                # Разделяем строку на две части и рекурсивно ищем в них
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                # Возвращаем самую длинную подстроку
                return left if len(left) >= len(right) else right
        
        # Если вся строка "красивая"
        return s





s = "YazaAay"
example = Solution()
result1 = example.longestNiceSubstring(s)
print(result1)

s = "Bb"
result2 = example.longestNiceSubstring(s)
print(result2)

s = "c"
result3 = example.longestNiceSubstring(s)
print(result3)