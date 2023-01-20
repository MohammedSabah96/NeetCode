# Given an integer array nums, return all the triplets [nums[i],
# nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []

# Constraints:
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    @staticmethod
    def three_sum(nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = num + nums[left] + nums[right]

                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result


sol = Solution()

nums_list = [-1, 0, 1, 2, -1, -4]
print(sol.three_sum(nums_list))
nums_list = [0]
print(sol.three_sum(nums_list))
nums_list = []
print(sol.three_sum(nums_list))
