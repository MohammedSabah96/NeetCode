# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

def is_anagram(s_string: str, t_string: str) -> bool:
    if len(s_string) != len(t_string):
        return False

    for char in set(s_string):
        if s_string.count(char) != t_string.count(char):
            return False
    else:
        return True


s = "anagram"
t = "nagaram"
print(is_anagram(s, t))

s = "rat"
t = "car"
print(is_anagram(s, t))
