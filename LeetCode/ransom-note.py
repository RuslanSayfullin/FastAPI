"""
Для двух строк: ransomNote и magazine, верните значение true, если ransomNote можно составить из букв из magazine, и false в противном случае.
Каждая буква из magazine может быть использована в ransomNote только один раз.
"""
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Считаем количество каждой буквы в ransomNote и magazine
        note_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        # Проверяем, хватает ли букв из magazine для ransomNote.
        for char, needed in note_count.items():
            if magazine_count[char] < needed:
                return False
            
        return True
          
          





ransomNote = "a"
magazine = "b"
example = Solution()
result1 = example.canConstruct(ransomNote, magazine)
print(result1)

ransomNote = "aa"
magazine = "ab"
example = Solution()
result2 = example.canConstruct(ransomNote, magazine)
print(result2)

ransomNote = "aa"
magazine = "aab"
example = Solution()
result3 = example.canConstruct(ransomNote, magazine)
print(result3)