# -*- coding: utf-8 -*-
# Copyright (c) 2019 Ascentio Technologies S.A. All rights reserved.
#
# This program is confidential and proprietary to Ascentio Technologies S.A.,
# and may not be copied, reproduced, modified, disclosed to
# others, published or used, in whole or in part, without the
# express prior written permission of Ascentio Technologies S.A.

import unittest
from thingsboard_cli import version as module_version

__copyright__ = 'Copyright (c) 2019 Ascentio Technologies S.A.'


class VersionTests(unittest.TestCase):

    def test_version_is_valid(self):
      self.assertIsNotNone(module_version)

if __name__ == "__main__":
    unittest.main()
