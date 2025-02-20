import os

import pytest

from gendiff.scripts.gendiff import generate_diff

TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), 'test_data')


def make_path(file):
    return os.path.join(TEST_DATA_PATH, file)


def read_file(file_path):
    with open(file_path) as f:
        return f.read()


@pytest.mark.parametrize("file1, file2, formatter, expected", [
    (make_path("file3.json"), make_path("file4.json"), 'stylish',
     make_path("expected_stylish.txt")),
    (make_path("file3.yml"), make_path("file4.yaml"), 'stylish',
     make_path("expected_stylish.txt")),
    (make_path("file3.json"), make_path("file4.json"), 'plain',
     make_path("expected_plain.txt")),
    (make_path("file3.yml"), make_path("file4.yaml"), 'plain',
     make_path("expected_plain.txt")),
    (make_path("file3.json"), make_path("file4.json"), 'json',
     make_path("expected_json.txt")),
    (make_path("file3.yml"), make_path("file4.yaml"), 'json',
     make_path("expected_json.txt")),
])
def test_generate_diff(file1, file2, formatter, expected):
    diff = generate_diff(file1, file2, formatter)
    expected_result = read_file(expected)
    assert diff == expected_result
