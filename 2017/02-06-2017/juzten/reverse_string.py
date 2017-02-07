#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Name:  Justin Spain
# Email: juzten@gmail.com
# Date:  02/07/2017
# Python Version: 3.5.1
#-----------------------------------------------------------------------------

# Chadev Python Weekly Challenge

# Problem: Reverse String
# CHALLENGE DESCRIPTION:

# You are given a list of strings that need to be reversed.
# Needs to handle multiple words, but the order of the words needs to stay the same.
# Your program should accept as its first argument a path to a filename.

# Input example: words.py
# python
# chadev
# civic
# branching
# multiple words
# reverse all the things

# Output Example:
# noitanibmoc
# nohtyp
# vedahc
# civic
# gnihcnarb
# elpitlum sdrow
# esrever lla eht sgniht

# Command to run program: python reverse_string.py words.py

#-----------------------------------------------------------------------------
# Begin the main program.
#-----------------------------------------------------------------------------

import sys
test_cases = open(sys.argv[1], 'r')
for line in test_cases:
    words = line.rstrip('\n').split(' ')
    output = ''
    for word in words:
        output = output + word[::-1] + ' '
    output.rstrip(' ')
    print(output)
test_cases.close()
