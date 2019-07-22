#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018--2023, Wang Weihua.
# All rights reserved.
message = input('请输入明文：')
message = message.upper()

key = input('请输入凯撒密码数（1-26）：')
key = int(key)

translated = ''
for c in message:
    if c.isalpha():
        num = ord(c) + key
        if num > ord('Z'):
            num -= 26
        translated += chr(num)
    else:
        translated += c
print('加密文：', translated)