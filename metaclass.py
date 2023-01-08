# Создать метакласс для паттерна Синглтон (см. конец вебинара)

class MyMetaClass(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance 


class MyTest(metaclass=MyMetaClass):
    pass


a = MyTest()
b = MyTest()
c = MyTest()
print('a is b is c —', a is b is c)