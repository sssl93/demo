#!/usr/bin/env python
# coding:utf-8


class AlertHandle(object):
    def send_email(self):
        pass

    def send_message(self):
        pass


class ServiceHandle(object):
    def stop_service(self):
        pass

    def start_service(self):
        pass

    def restart_service(self):
        pass
