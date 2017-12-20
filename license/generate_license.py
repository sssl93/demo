#!/usr/bin/env python
# coding:utf-8

from collections import OrderedDict
from license.utils.signature_utils import signature_instance


class LicenseBase(object):

    def __init__(self, file_path, license_info=None):
        self.file_path = file_path
        self.license_info = license_info

    def _load_file(self):
        with open(self.file_path, "rb") as f:
            file_lines = [line.strip() for line in f]
        message = ','.join(file_lines)
        return message

    def _load_message(self, message):
        license_info = OrderedDict()
        for item in message.split(','):
            k, v = item.split('=', 1)
            license_info[k] = v
        return license_info

    def _get_items(self, license_info):
        items = []
        for k, v in license_info.items():
            items.append('%s=%s' % (k, v))
        return items

    def _format_message(self, license_info):
        items = self._get_items(license_info)
        message = ','.join(items)
        return message

    def _check_signature(self, message, signature):
        return signature_instance.verify(message=message, signature=signature)

    def generate_license_file(self):
        items = self._get_items(self.license_info)
        with open(self.file_path, 'wb+') as f:
            for item in items:
                f.writelines(item + '\n')
        return True

    def load_license_file(self):
        message = self._load_file()
        license_info = self._load_message(message)
        if 'signature' not in license_info:
            raise Exception("could not find the license signature!")
        signature = license_info.pop('signature', '')
        message = self._format_message(license_info)
        if not self._check_signature(message, signature):
            raise Exception("the license signature is not correct! please contact the administrator")
        return dict(license_info)

    def add_signature(self, hash_type):
        message = self._format_message(self.license_info)
        signature = signature_instance.generate_sign_string(message, hash_type=hash_type)
        self.license_info['signature'] = signature
        return True

    def encrypt_content(self):
        pass

    def decrypt_content(self):
        pass
