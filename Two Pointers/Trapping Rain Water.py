# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
#
# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution:
    @staticmethod
    def trap(height: list[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left = height[left]
        max_right = height[right]
        res = 0

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                res += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                res += max_right - height[right]

        return res


sol = Solution()

h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # output = 6
print(sol.trap(h))
h = [4, 2, 0, 3, 2, 5]  # output = 9
print(sol.trap(h))
h = [4, 2, 3]  # output = 1
print(sol.trap(h))
