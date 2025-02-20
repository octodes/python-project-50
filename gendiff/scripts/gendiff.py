import argparse

from gendiff.find_diff import find_diff
from gendiff.formatters.json_format import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.parser import parse


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    diff = find_diff(data1, data2)

    match format_name:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'basic':
            return diff
        case 'json':
            return json_format(diff)
        case _:
            raise ValueError(f"Unknown format type: {format_name}")


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        choices=[
            'basic',
            'json',
            'plain',
            'stylish',
        ],
        help='set format of output',
    )

    args = parser.parse_args()

    file_path1 = args.first_file
    file_path2 = args.second_file
    formatter = args.format

    print(generate_diff(file_path1, file_path2, formatter))


if __name__ == '__main__':
    main()
