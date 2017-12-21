#!/usr/bin/env python
# coding:utf-8


class LicenseCheckError(Exception, object):
    """The base exception class for all license check exceptions ."""

    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return repr(self.message)


class ResourceRestrictionError(LicenseCheckError):

    def __init__(self, message='the resource restriction ! please extend resource', code=60001):
        super(ResourceRestrictionError, self).__init__(message, code)


class ExpirationTimeError(LicenseCheckError):

    def __init__(self, message='expiration time restriction ! please renewal fees', code=60002):
        super(ExpirationTimeError, self).__init__(message, code)


class FirstUseTimeError(LicenseCheckError):

    def __init__(self, message='first use time restriction ! please reset your local time', code=60003):
        super(FirstUseTimeError, self).__init__(message, code)


class MaxUsedTimeError(LicenseCheckError):

    def __init__(self, message='max used time restriction ! please renewal fees', code=60004):
        super(MaxUsedTimeError, self).__init__(message, code)
