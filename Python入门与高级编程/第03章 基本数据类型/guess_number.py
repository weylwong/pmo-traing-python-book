#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018--2023, Wang Weihua.
# All rights reserved.
import random

name = input("请问阁下尊姓大名？")
print('您好！', name)
print('欢迎来到猜数字游戏，数字范围在1到100之间')

target_number = random.randint(1, 100)
for i in range(8):
    guess_number = input('猜一个数字：')
    guess_number = int(guess_number)
    if guess_number == target_number:
        break
    elif guess_number > target_number:
        print('猜大了')
    else:
        print('猜小了')       
        
if guess_number == target_number:
    print('您太厉害了！猜了', i+1, '次')        
else:
    print('您需要努力啊')            
    print('要猜的数字是', target_number)  