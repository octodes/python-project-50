import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', required=False, help='set format of output')

    args = parser.parse_args()

    path1 = args.first_file
    path2 = args.second_file

    file1 = json.load(open(path1))
    file2 = json.load(open(path2))



if __name__ == '__main__':
    main()