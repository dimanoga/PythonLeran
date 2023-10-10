"""Given an integer array nums, return true if any value appears at least twice in the array,
 and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 """
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    set_nums = set({})
    for num in nums:
        if num not in set_nums:
            set_nums.add(num)
        else:
            return True
    return False


def contains_duplicate2(nums: List[int]) -> bool:
    for num in nums:
        if nums.count(num) > 1:
            return True
    return False

