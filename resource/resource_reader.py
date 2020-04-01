#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class ResourceReader(object):

    def get_resource_path(self, relative_resource):
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, relative_resource)
        return path

    def open_resource(self, relative_resource, mode, encoding='utf-8'):
        return open(self.get_resource_path(relative_resource), mode, encoding=encoding)
