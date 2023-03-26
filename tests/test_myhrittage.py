import filecmp
import os
from deepdiff import DeepDiff
import assertion_manager
import pytest


## In this tests we will check if the file of our actual results is exists
def test_check_if_file_of_pricing_list_is_exists():
    check_if_exists = os.path.exists(os.path.join("..", "pricing_list.txt"))
    assert check_if_exists == True, assertion_manager.file_is_not_exists()

## In this test we will check using deepDiff python package by comparing 2 texts file (expected and actual)
def test_check_if_content_in_text_file_correct(test_cases_setup):
    actual_results = os.path.join(os.curdir,"pricing_list.txt")
    expected_results = os.path.join(os.curdir,"expected_result.txt")
    result = filecmp.cmp(expected_results, actual_results, shallow=False)
    assert result, assertion_manager.files_are_not_the_same()
