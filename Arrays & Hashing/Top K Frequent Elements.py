# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
# Example 1:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# 1 <= nums.length <= 105
# k is in the range[1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

from collections import Counter


def topk_frequent(nums_list: list[int], k_int: int) -> list[int]:
    li_of_tup = Counter(nums_list).most_common(k_int)
    ans = []
    for num_count in li_of_tup:
        ans.append(num_count[0])
    return ans

# O(nlogn)
# def topk_frequent(nums_list: list[int], k_int: int) -> list[int]:
#     num_dict = {}
#     for num in nums_list:
#         if num not in num_dict:
#             num_dict[num] = 1
#         else:
#             num_dict[num] += 1
#
#     return (sorted(num_dict, key=num_dict.get, reverse=True))[0:k_int]

# O(n)
# def topk_frequent(nums_list: list[int], k_int: int) -> list[int]:
#     count = {}
#     freq = [[] for i in range(len(nums_list) + 1)]
#     for n in nums:
#         count[n] = 1 + count.get(n, 0)
#
#     for n, c in count.items():
#         freq[c].append(n)
#
#     res = []
#     for i in range(len(freq) - 1, 0, -1):
#         for n in freq[i]:
#             res.append(n)
#             if len(res) == k_int:
#                 return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topk_frequent(nums, k))
nums = [1]
k = 1
print(topk_frequent(nums, k))
nums = [3, 0, 1, 0]
k = 1
print(topk_frequent(nums, k))
