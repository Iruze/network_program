#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def zzw_application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ.get('PATH_INFO')
    path = 'man' if path == '/' else path.lstrip('/')
    #return [b'<h1>Hello world!</h1>']
    
    with open('./welcome.html', 'r') as f:
        data = f.read() % path
    return [data.encode('utf-8')]

