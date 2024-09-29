# coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class A:
    _data = 1

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

