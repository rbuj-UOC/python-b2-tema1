import pytest
from ej1c1 import quicksort, mergesort, merge  

@pytest.mark.parametrize("test_input,expected,message", [
    ([], [], "Quicksort should return an empty list when the input is empty."),
    ([1], [1], "Quicksort should return a single-element list unchanged."),
    ([2, 1], [1, 2], "Quicksort should correctly sort a list of two elements."),
    ([3, 1, 2], [1, 2, 3], "Quicksort should correctly sort a list of three elements."),
    ([9, 3, 5, 1, 4, 2, 6, 8, 7], [1, 2, 3, 4, 5, 6, 7, 8, 9], "Quicksort should correctly sort a list of multiple elements."),
    (list(range(10, 0, -1)), list(range(1, 11)), "Quicksort should correctly sort a list in descending order.")
])
def test_quicksort(test_input, expected, message):
    assert quicksort(test_input) == expected, message

@pytest.mark.parametrize("test_input,expected,message", [
    ([], [], "Mergesort should return an empty list when the input is empty."),
    ([1], [1], "Mergesort should return a single-element list unchanged."),
    ([2, 1], [1, 2], "Mergesort should correctly sort a list of two elements."),
    ([3, 1, 2], [1, 2, 3], "Mergesort should correctly sort a list of three elements."),
    ([9, 3, 5, 1, 4, 2, 6, 8, 7], [1, 2, 3, 4, 5, 6, 7, 8, 9], "Mergesort should correctly sort a list of multiple elements."),
    (list(range(10, 0, -1)), list(range(1, 11)), "Mergesort should correctly sort a list in descending order.")
])
def test_mergesort(test_input, expected, message):
    assert mergesort(test_input) == expected, message

@pytest.mark.parametrize("left,right,expected,message", [
    ([1], [2], [1, 2], "Merge should correctly combine two single-element lists."),
    ([2, 3], [1], [1, 2, 3], "Merge should place all elements from the second list before the first if they are smaller."),
    ([1, 3], [2, 4], [1, 2, 3, 4], "Merge should interleave elements from both lists when they alternate in order."),
    ([], [1, 2, 3], [1, 2, 3], "Merge should return the non-empty list when one list is empty."),
    ([1, 2, 3], [], [1, 2, 3], "Merge should return the non-empty list when the other list is empty.")
])
def test_merge(left, right, expected, message):
    assert merge(left, right) == expected, message
