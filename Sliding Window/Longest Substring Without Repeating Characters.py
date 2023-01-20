# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        char_set = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right - left + 1)

        return res


sol = Solution()

string = "abcabcbb"
print(sol.length_of_longest_substring(string))  # Output = 3
string = "bbbbb"
print(sol.length_of_longest_substring(string))  # Output = 1
string = "pwwkew"
print(sol.length_of_longest_substring(string))  # Output = 3
string = "au"
print(sol.length_of_longest_substring(string))  # Output = 2
string = "dvdf"
print(sol.length_of_longest_substring(string))  # Output = 3
