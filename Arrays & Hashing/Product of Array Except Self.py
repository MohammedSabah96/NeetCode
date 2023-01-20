# Given an integer array nums,
# return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32 - bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Example 1:
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

# Example 2:
# Input: nums = [-1, 1, 0, -3, 3]
# Output: [0, 0, 9, 0, 0]

# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32 - bit integer.

def product_except_self(nums_list: list[int]) -> list[int]:
    n = len(nums_list)
    res = [1] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums_list[i]

    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums_list[i]

    return res


nums = [1, 2, 3, 4]
print(product_except_self(nums))
nums = [-1, 1, 0, -3, 3]
print(product_except_self(nums))
