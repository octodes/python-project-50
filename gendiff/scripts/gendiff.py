import argparse
from gendiff.parser import parse
from gendiff.find_diff import find_diff


def generate_diff(file_path1, file_path2):
    data1 = parse(file_path1)
    data2 = parse(file_path2)

    result = find_diff(data1, data2)
    print(result)
    return None


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', required=False, help='set format of output')

    args = parser.parse_args()

    file_path1 = args.first_file
    file_path2 = args.second_file

    generate_diff(file_path1, file_path2)


if __name__ == '__main__':
    main()
