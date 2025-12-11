"""
Даны две строки s и t. Верните true, если t является анаграммой строки s, и false в противном случае.
Анаграмма — это слово или фраза, образованная путем перестановки букв другого слова или фразы с использованием всех исходных букв ровно один раз.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        else:
            s2 = list(s)
            t2 = list(t)

            for i in t2:
                if i in s2:
                    s2.remove(i)
                else:
                    return False
                
            return True


s = "anagram"
t = "nagaram"
example =Solution()
result1 = example.isAnagram(s, t)
assert result1 == True
print(result1)

s = "rat"
t = "car"
result2 = example.isAnagram(s, t)
assert result2 == False
print(result2)