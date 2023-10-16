from typing import List

import pytest

from LeetCode.disappeared_numbers import find_disappeared_numbers


@pytest.mark.parametrize("input_values,expected", [
    ([4,3,2,7,8,2,3,1], [5,6]),
    ([1,1], [2])
])
def test_disappeared_numbers(input_values: List[int], expected: bool):
    assert find_disappeared_numbers(nums=input_values) == expected
