from typing import List

import pytest

from LeetCode.missing_number import missing_number2


@pytest.mark.parametrize("input_values,expected", [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
])
def test_missing_number(input_values: List[int], expected: bool):
    # assert missing_number(nums=input_values) == expected
    assert missing_number2(nums=input_values) == expected
