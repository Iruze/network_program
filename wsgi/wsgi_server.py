#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from hello import zzw_application

httpd = make_server('', 8080, zzw_application)
print('serving HTTP on port 8080...')

httpd.serve_forever()

