#!/usr/bin/env python3
import argparse


def search_in_file(file_name, search_str):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if search_str in line:
                print(line, end='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Search a file for lines containing pattern")
    parser.add_argument('--file', type=str, default='./config.txt', help="Path to file")
    parser.add_argument('--pattern', type=str, default='path', help="Word to search for")

    args = parser.parse_args()
    file = args.file
    pattern = args.pattern

    search_in_file(file, pattern)
