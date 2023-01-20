# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


def is_palindrome(s: str) -> bool:
    left: int = 0
    right: int = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while right > left and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


class Solution:
    def is_palindrome(self, s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1
        while left < right:
            while left < right and not self.is_alphanum(s[left]):
                left += 1
            while right > left and not self.is_alphanum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    @staticmethod
    def is_alphanum(c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))


sol = Solution()

s_str = "A man, a plan, a canal: Panama"
print(sol.is_palindrome(s_str))

s_str = "race a car"
print(sol.is_palindrome(s_str))

s_str = " "
print(sol.is_palindrome(s_str))

s_str = "Marge, let's \"[went].\" I await {news} telegram."
print(sol.is_palindrome(s_str))

s_str = "`l;`` 1o1 ??;l`"
print(sol.is_palindrome(s_str))
