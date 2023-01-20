# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

class Solution:
    @staticmethod
    def max_area(height: list[int]) -> int:
        maximum_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            maximum_area = max(area, maximum_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum_area


sol = Solution()

h = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # output = 49
print(sol.max_area(h))
h = [1, 1]  # output = 1
print(sol.max_area(h))
h = [2, 3, 4, 5, 18, 17, 6]  # output = 17
print(sol.max_area(h))
h = [1, 3, 2, 5, 25, 24, 5]  # output = 24
print(sol.max_area(h))
