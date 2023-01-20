# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

# Example 3:
# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

def contains_duplicate(nums_list: list[int]) -> bool:
    # n = len(nums_list)
    # if n == 0 or n == 1:
    #     return False
    # return n != len(set(nums_list))

    dic = {}
    for num in nums_list:
        if num not in dic:
            dic[num] = 1
        else:
            return True
    else:
        return False


nums = [1, 2, 3, 1]
print(contains_duplicate(nums))
nums = [1, 2, 3, 4]
print(contains_duplicate(nums))
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(contains_duplicate(nums))
