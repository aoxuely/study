# encoding:utf8
"""
修改变量的三种方式
1. 通过类名直接修改类变量
2. 通过classmethod装饰的类方法读取类变量，需要注意的是，如果被子类继承，此时读取得到的是子类变量值，因为传入的cls为子类
3. 通过propert装饰的类属性函数读取类变量，这种方法本质和第二点逻辑一致

注意第3点，类属性在 Python 3.11 中已弃用，在 Python 3.13 中将不受支持
"""

class A(object):
    _val = "this is default value"
    
    @classmethod
    def set_val(cls, v):
        cls._val = v

if  __name__ == "__main__":
    print(A._val)
    
    A._val = "this is new value"
    print(A._val)
    
    A.set_val("this is new value again")
    print(A._val)
    

"""
this is default value
this is new value
this is new value again
"""