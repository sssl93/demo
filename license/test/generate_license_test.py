#!/usr/bin/env python
# coding:utf-8

import unittest, os, copy
from license.generate_license import LicenseBase

FILE_PATH = '/tmp/testLicense.li'
LICENSE_INFO = {
    "name": "License Info",
    "CPU": '10',
    "expired_date": "2018-1-1 23:59:59",
    "used_time": '600'
}


class TestLicenseBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestLicenseBase, cls).setUpClass()

        cls.license = LicenseBase(file_path=FILE_PATH, license_info=copy.deepcopy(LICENSE_INFO))

    @classmethod
    def tearDownClass(cls):
        # os.remove(FILE_PATH)
        pass

    def test_generate_license_file(self):
        result = self.license.generate_license_file()
        self.assertEqual(True, result)

    def test_load_license_file(self):
        result = self.license.load_license_file()
        self.assertDictEqual(LICENSE_INFO, result)

    def test_add_signature(self):
        result = self.license.add_signature('SHA-256')
        self.assertEqual(True, result)


if __name__ == "__main__":
    unittest.main()
