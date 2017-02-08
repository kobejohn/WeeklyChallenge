#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Inline string reverser

Usage:
  reverse_string.py <input_path>

Options:
  -h --help     Show this screen.

"""
from docopt import docopt


def main():
    input_path = docopt(__doc__)['<input_path>']
    with open(input_path, 'r') as f:
        for line in f:
            print(reverse_line(line))


def reverse_line(line):
    return ' '.join(''.join(reversed(word)) for word in line.split())


if __name__ == '__main__':
    main()
