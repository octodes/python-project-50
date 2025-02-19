import os
import json

from gendiff.scripts.gendiff import generate_diff

TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), 'test_data')

def read_test_data(file_path):
    with open(file_path) as f:
        return f.read()

def test_flat_diff_json():
    file_path1 = os.path.join(TEST_DATA_PATH, 'file1.json')
    file_path2 = os.path.join(TEST_DATA_PATH, 'file2.json')
    expected_result = read_test_data(os.path.join(TEST_DATA_PATH, 'json_plain_result.txt'))
    result = generate_diff(file_path1, file_path2)
    assert result == expected_result