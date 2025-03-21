# encoding:utf8
"""
父类如果定义了类变量，子类也能访问该变量

子类的类变量遵循写时复制的原则，
即子类实例化时，如果父类中定义了类变量，则子类中不存在类变量，
访问该变量得到的是父类变量，父类变量发生变化，此时通过子类访问该类变量值也会发生改变

但当通过子类的方法修改类变量时，会复制一个变量保存子类变量值
此后，父类变量的修改不影响子类变量

不过，如果子类在继承父类时重新定义了该类变量，则不遵循写时复制原则，默认的类变量就和父类变量不同

由于写时复制的原则，子类不能直接修改父类的类变量，一旦修改则会复制一个变量保存子类变量值
不过，当类变量保存的数据类型为list、set、dict等引用类型时，通过子类变量可以直接修改父类变量引用变量内部的值
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