#!/usr/bin/env python3 该行应该为注释不可以去掉注释为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# -*- coding: utf-8 -*- 该行应该为注释不可以去掉注释

# import matplotlib.pyplot as plt
#
#
# # hw model - synthesizable operations only
# def shift_right_arith(val, n):  # right arithmetic shift – use “>>>” operation in SystemVerilog
#     return val >> n
#
#
# def cordic_iteration(angle):
#     atan_table = [0xc910, 0x76b2, 0x3eb7, 0x1fd6,
#                   0x0ffb, 0x07ff, 0x0400, 0x0200,
#                   0x0100, 0x0080, 0x0040, 0x0020,
#                   0x0010, 0x0008, 0x0004, 0x0002]
#
#     x = 65536
#     y = 0
#     z = angle
#
#     for i in range(0, 16):
#         if z <= 0:
#             d = -1
#         else:
#             d = 1
#
#         nextx = x - shift_right_arith((y * d), i)
#         nexty = y + shift_right_arith((x * d), i)
#
#         x = nextx
#         y = nexty
#         z = z - (d * atan_table[i])
#     return x
#
# #generating test stimulus
# x = []
# y = []
# for index in range(0, 98304, 128):
#     x.append(index)
#     y.append(cordic_iteration(index))
# print(y)
# plt.plot(x, y)
# # plt.show()

# import torch
# print(torch.backends.mps.is_available())

# args = ['gcc', 'hello.c', 'world.c',"jiangwu"]
# a, file1, *files=args
# print('hello.c'+","+','.join(files))
# d={1:2}
# print(d.get(2))
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# fib(6)
import this
