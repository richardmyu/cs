# -*- coding: utf-8 -*-

import unittest
from python_repos import get_url_info


class NamesTestCase(unittest.TestCase):

    def test_200(self):
        r = get_url_info()
        self.assertEqual(200, r.status_code)


unittest.main()
