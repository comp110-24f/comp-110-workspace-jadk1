from exercises.ex05.utils import only_evens, sub, add_at_index


# only_evens testing
# Use case 1
def test_only_evens_odd_and_even():
    """only_evens should return only evens given a mix of odds and evens."""
    """only_evens should not mutate the input list."""
    ex_list = [1, 2, 3, 4, 5]
    assert only_evens(ex_list) == [2, 4]
    assert ex_list == [1, 2, 3, 4, 5]


# Use case 2
def test_only_evens_all_evens():
    """only_evens should return the entire input list if all even."""
    assert only_evens([2, 4, 6, 8, 10]) == ([2, 4, 6, 8, 10])


# Edge case
def test_only_evens_only_odds():
    """only_evens should return an empty string if input is only odd."""
    assert only_evens([1, 3, 5, 7]) == []


# sub testing
# Use case 1
def test_sub_valid_range():
    """Sub should return correct elements given a valid range within bounds."""
    """Sub should not mutate the input list"""
    ex_list = [100, 200, 300, 400, 500]
    assert sub(ex_list, 1, 4) == [200, 300, 400]
    assert ex_list == [100, 200, 300, 400, 500]


# Use case 2
def test_sub_index_greater_than_list_length():
    """Sub should begin with end of list if end index > len of list."""
    assert sub([100, 200, 300], 1, 10) == [200, 300]


# Edge case
def test_sub_negative_start():
    assert sub([100, 200, 300, 400], -3, 3) == [100, 200, 300]


# add_at_index testing
# Use case 1
def test_add_at_index_middle():
    """add_at_index should work normally with elem inserted in middle index."""
    ex_list = [10, 20, 30, 50]
    add_at_index(ex_list, 40, 3)
    assert ex_list == [10, 20, 30, 40, 50]


# Use case 2
def test_add_at_index_mutate_list():
    """add_at_index should mutate the input list"""
    ex_list = [10, 20, 30, 50]
    add_at_index(ex_list, 1000, 4)
    assert ex_list != [10, 20, 30, 50]


# Edge case
def test_add_at_index_empty_list():
    """add_at_index should add an element to an empty list at index 0"""
    ex_list = []
    add_at_index(ex_list, 50, 0)
    assert ex_list == [50]
