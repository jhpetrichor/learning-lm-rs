'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2025-01-07 16:45:26
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2025-01-07 16:56:37
FilePath: /learning-lm-rs/test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AEnum
'''
import numpy as np

def sigmoid(x, y):
    a = 1 / (1 + np.exp(-x))
    print(a)
    b = a * x
    print(b)
    c = b * y
    print(c)
    return c    
    # return 1 / (1 + np.exp(x)) * x * y


a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
sigmoid_x = sigmoid(a, b)
print(sigmoid_x)