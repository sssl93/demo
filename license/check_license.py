#!/usr/bin/env python
# coding:utf-8


from license.config import NODE_ITEMS
from license.exceptions import ResourceRestrictionError, ExpirationTimeError, FirstUseTimeError, MaxUsedTimeError
from datetime import datetime


class CheckLicense(object):
    def __init__(self, license_info, node_info):
        self.license_info = license_info
        self.node_info = node_info
        self.exception_pool = []

    def _check_license_content(self):
        string_list, result = [], None
        for item in NODE_ITEMS:
            name = item['name']
            unit = item['unit']
            node_value = self.node_info.get(name)
            license_value = self.license_info.get(name)
            if node_value > license_value:
                string_list.append("%s resource restriction ! MAX:%s%s NOW:%s%s" %
                                   (name, license_value, unit, node_value, unit))
        if string_list:
            result = ResourceRestrictionError("\n".join(string_list))
            self.exception_pool.append(result)
        return result

    def _check_expiration_time(self):
        result = None
        expiration_time = datetime.strptime(self.license_info["expiration_time"], "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        if now > expiration_time:
            result = ExpirationTimeError("expiration time restriction ! Expiration Time:%s Now:%s" %
                                         (self.license_info["expiration_time"], now.strftime("%Y-%m-%d %H:%M:%S")))
            self.exception_pool.append(result)
        return result

    def _check_first_use_time(self):
        result = None
        first_use_time = datetime.strptime(self.license_info["first_use_time"], "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        if now < first_use_time:
            result = FirstUseTimeError("first use time restriction ! First Use Time:%s Now:%s" %
                                       (self.license_info["first_use_time"], now.strftime("%Y-%m-%d %H:%M:%S")))
            self.exception_pool.append(result)
        return result

    def _check_max_used_time(self):
        result = None
        used_time = self.license_info['used_time']
        max_used_time = self.license_info['max_used_time']
        if used_time > max_used_time:
            result = MaxUsedTimeError("max used time restriction ! Max Use Time:%s Used Time:%s" %
                                      (max_used_time, used_time))
            self.exception_pool.append(result)

        return result

    def run(self):
        self._check_first_use_time()
        self._check_expiration_time()
        self._check_max_used_time()
        self._check_license_content()
        return self.exception_pool
