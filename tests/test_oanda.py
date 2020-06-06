# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Test functions for supplai module
"""

import unittest
from supplai_client import supplai


class TestOandaApi(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        a = supplai.APIv20(access_token="test")
        self.assertIsNotNone(a)

    def tearDown(self):
        pass

    def test_name(self):
        pass
