#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_strf
----------------------------------

Tests for `strf` module.
"""
from strf import strf
import unittest


class TestStrf(unittest.TestCase):
    def test_strf(self):
        # define a function to open a local namespace
        def test_closure(test_arg, test_kwarg=2):
            local_var = '3'
            return strf('{test_arg}{test_kwarg}{local_var}')
        
        self.assertEqual(test_closure(1), '123')

if __name__ == '__main__':
    unittest.main()