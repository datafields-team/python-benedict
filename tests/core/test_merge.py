# -*- coding: utf-8 -*-

from benedict.core import merge as _merge

import unittest


class merge_test_case(unittest.TestCase):

    def test_merge_with_flatten_dict(self):
        d = {
            'a': 1,
            'b': 1,
        }
        m = {
            'b': 2,
            'c': 3,
        }
        _merge(d, m)
        r = {
            'a': 1,
            'b': 2,
            'c': 3,
        }
        self.assertEqual(d, r)

    def test_merge_with_multiple_dicts(self):
        d = {
            'a': 1,
            'b': 1,
        }
        a = {
            'b': 2,
            'c': 3,
            'd': 3,
        }
        b = {
            'd': 5,
            'e': 5,
        }
        c = {
            'd': 4,
            'f': 6,
        }
        _merge(d, a, b, c)
        r = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
        }
        self.assertEqual(d, r)

    def test_merge_with_nested_dict(self):
        d = {
            'a': 1,
            'b': {
                'c': {
                    'x': 2,
                    'y': 3,
                },
                'd': {
                    'x': 4,
                    'y': 5,
                },
                'e': {
                    'x': 6,
                    'y': 7,
                },
            },
        }
        m = {
            'a': 0,
            'b': {
                'c': 1,
                'd': {
                    'y': 1,
                    'z': 2,
                },
                'e': {
                    'f': {
                        'x': 2,
                        'y': 3,
                    },
                    'g': {
                        'x': 4,
                        'y': 5,
                    },
                },
            },
        }
        _merge(d, m)
        r = {
            'a': 0,
            'b': {
                'c': 1,
                'd': {
                    'x': 4,
                    'y': 1,
                    'z': 2,
                },
                'e': {
                    'f': {
                        'x': 2,
                        'y': 3,
                    },
                    'g': {
                        'x': 4,
                        'y': 5,
                    },
                    'x': 6,
                    'y': 7,
                },
            },
        }
        self.assertEqual(d, r)
