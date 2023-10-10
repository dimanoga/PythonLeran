from typing import List

import pytest

from LeetCode.containsDuplicate import contains_duplicate, contains_duplicate2


@pytest.mark.parametrize("input_values,expected", [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
])
def test_duplicate(input_values: List[int], expected: bool):
  #  assert contains_duplicate(nums=input_values) == expected
    assert contains_duplicate2(nums=input_values) == expected
