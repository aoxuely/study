# coding=utf-8
"""
运行结果：
2024-09-29 20:12:26,457 - root - INFO - set A data to 2
2024-09-29 20:12:26,457 - root - INFO - A._data=2,id=140518361174720
2024-09-29 20:12:26,457 - root - INFO - B._data=2,id=140518361174720
2024-09-29 20:12:26,457 - root - INFO - inst A._data=2,id=140518361174720
2024-09-29 20:12:26,457 - root - INFO - set A data to 1
2024-09-29 20:12:26,457 - root - INFO - A._data=1,id=140518361174744
2024-09-29 20:12:26,457 - root - INFO - B._data=1,id=140518361174744
2024-09-29 20:12:26,457 - root - INFO - inst A._data=1,id=140518361174744
2024-09-29 20:12:26,457 - root - INFO - set B data to 3
2024-09-29 20:12:26,457 - root - INFO - A._data=1,id=140518361174744
2024-09-29 20:12:26,457 - root - INFO - B._data=3,id=140518361174696
2024-09-29 20:12:26,457 - root - INFO - inst B._data=3,id=140518361174696
2024-09-29 20:12:26,457 - root - INFO - set A data to 4
2024-09-29 20:12:26,458 - root - INFO - A._data=4,id=140518361174672
2024-09-29 20:12:26,458 - root - INFO - B._data=3,id=140518361174696
2024-09-29 20:12:26,458 - root - INFO - inst A._data=4,id=140518361174672
2024-09-29 20:12:26,458 - root - INFO - set B data to 5
2024-09-29 20:12:26,458 - root - INFO - A._data=4,id=140518361174672
2024-09-29 20:12:26,458 - root - INFO - B._data=5,id=140518361174648
2024-09-29 20:12:26,458 - root - INFO - inst B._data=5,id=140518361174648

结论：
    1. 类成员变量与类绑定，继承时从父类继承对应变量和值
    2.
"""

import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class A:
    _data = 1

    @classmethod
    def set_a_inner(cls, data):
        cls._data = data

    @classmethod
    def set_a_inner2(cls, data):
        A._data = data

    def __init__(self, data=None):
        if data:
            logging.info("set %s data to %s", self.__class__.__name__, data)
            self.set_a(data)
        log_a_and_b(self)

    @classmethod
    def set_a(cls, data):
        cls._data = data


class B(A):
    pass


def log_a_and_b(ins):
    logging.info("A._data=%s,id=%s", A._data, id(A._data))
    logging.info("B._data=%s,id=%s", B._data, id(B._data))
    logging.info("inst %s._data=%s,id=%s", ins.__class__.__name__, ins._data, id(ins._data))


if __name__ == '__main__':
    a = A(2)
    a = A(1)
    b = B(3)
    c = A(4)
    d = B(5)

