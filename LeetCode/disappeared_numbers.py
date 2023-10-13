"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""
from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        pos = nums[i] - 1  # Верная позиция. Например, 1 должна быть по индексу 0
        if nums[i] != nums[pos]:
            nums[i], nums[pos] = nums[pos], nums[i]
        else:
            i += 1
    missing_numbers = []
    for i in range(len(nums)):
        if nums[i] != i+1:
            missing_numbers.append(i+1)
    return missing_numbers

if __name__ == '__main__':
    find_disappeared_numbers(nums=[4,3,2,7,8,2,3,1])