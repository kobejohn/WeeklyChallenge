#!/usr/bin/env python
# -*- coding: utf-8 -*-
import contextlib
import io
from unittest import mock

import reverse_string


# reverse line ----------------------------------------------------------
def test_reverse_line_reverses_single_words():
    assert reverse_string.reverse_line('asdf') == 'fdsa'


def test_reverse_line_reverses_multiple_words():
    assert reverse_string.reverse_line('asdf jkl') == 'fdsa lkj'


def test_reverse_line_returns_empty_string_if_stripped_input_is_empty():
    assert reverse_string.reverse_line('   \t ') == ''


# main ----------------------------------------------------------
def test_main_reverses_text_in_input_file():
    # end to end test
    # patch docopt to provide a test file on input
    with mock.patch('reverse_string.docopt', ) as m_docopt:
        m_docopt.return_value.__getitem__.return_value = 'words.py'
        # patch stdout to a buffer that we can test
        out_buffer = io.StringIO()
        with contextlib.redirect_stdout(out_buffer):
            # capture the output when running main
            reverse_string.main()
    # get the output specification
    with open('words_solution.txt', 'r') as f:
        output_spec = f.read()
    assert out_buffer.getvalue() == output_spec
