"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""
import collections
from typing import List


def single_number(nums: List[int]) -> int:
    for item in collections.Counter(nums).items():
        if item[1] == 1:
            return item[0]


def single_number2(nums: List[int]) -> int:
    for num in nums:
        if nums.count(num) == 1:
            return num
    return 0


def single_number3(nums: List[int]) -> int:
    mask = 0
    for num in nums:
        mask ^= num
    return mask


if __name__ == '__main__':
    print(single_number2(nums=[4, 1, 2, 1, 2]))
