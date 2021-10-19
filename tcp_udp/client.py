#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket


# 创建连接的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接server
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))

for data in [b'Mike', b'David', b'Peter']:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

