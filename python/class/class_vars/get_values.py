# encoding:utf8
"""
读取类变量的三种方式
1. 通过类名直接读取类变量
2. 通过classmethod装饰的类方法读取类变量，需要注意的是，如果被子类继承，此时读取得到的是子类变量值，因为传入的cls为子类
3. 通过propert装饰的类属性函数读取类变量，这种方法本质和第二点逻辑一致

注意第3点，类属性在 Python 3.11 中已弃用，在 Python 3.13 中将不受支持

TODO:
子类继承父类，如果父类和子类都定义了同名类属性，
那么子类实例化时，读取类属性时，读取的是子类类属性，因为传入的cls为子类

子类的类变量遵循写时复制的原则，
即子类实例化时，如果父类中定义了类变量，则子类中不存在类变量，
访问该变量得到的是父类变量，父类变量发生变化，此时通过子类访问该类变量值也会发生改变

但当通过子类的方法修改类变量时，会复制一个变量保存子类变量值
此后，父类变量的修改不影响子类变量
"""

class A(object):
    _val = "this is value"
    
    @classmethod
    def get_val(cls):
        return cls._val
    
    @property
    def val(cls):
        return cls._val
    
    @classmethod
    def set_val(cls, val):
        cls._val = val

if  __name__ == "__main__":
    print(A._val)
    print(A.get_val())
    print(A().val)
    
"""
this is value
this is value
this is value
"""