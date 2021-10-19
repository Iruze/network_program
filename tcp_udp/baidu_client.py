#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# 建立socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.baidu.com', 80))

# 发送请求
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = list()
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

# 将请求到的body数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)

