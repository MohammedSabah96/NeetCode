# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every character
# in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.

class Solution:
    @staticmethod
    def min_window(s: str, t: str) -> str:
        if t == "":
            return ""
        count_t, window = {}, {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        return s[res[0]:res[1] + 1] if res_len != float("infinity") else ""


sol = Solution()

s_str = "ADOBECODEBANC"
t_str = "ABC"
print(sol.min_window(s_str, t_str))  # Output = "BANC"

s_str = "a"
t_str = "a"
print(sol.min_window(s_str, t_str))  # Output = "a"

s_str = "a"
t_str = "aa"
print(sol.min_window(s_str, t_str))  # Output = ""

s_str = "a"
t_str = "b"
print(sol.min_window(s_str, t_str))  # Output = ""
s_str = "acbbaca"
t_str = "aba"
print(sol.min_window(s_str, t_str))  # Output = "baca"
