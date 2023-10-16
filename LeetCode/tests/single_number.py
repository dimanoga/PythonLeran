from typing import List

import pytest

from LeetCode.single_number import single_number


@pytest.mark.parametrize("input_values,expected", [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1)
])
def test_single_number(input_values: List[int], expected: bool):
    assert single_number(nums=input_values) == expected
