import inspect


def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    info['attributes'] = [attr for attr in dir(obj) if not inspect.ismethod(getattr(obj, attr))]

    info['methods'] = [method for method in dir(obj) if inspect.ismethod(getattr(obj, method))]

    info['module'] = inspect.getmodule(obj).__name__

    if isinstance(obj, type):
        info['bases'] = [base.__name__ for base in obj.__bases__]
        info['mro'] = [cls.__name__ for cls in obj.mro()]
        info['class_doc'] = inspect.getdoc(obj)
    elif inspect.isfunction(obj) or inspect.ismethod(obj):
        info['source'] = inspect.getsource(obj)
        info['doc'] = inspect.getdoc(obj)
    elif inspect.ismodule(obj):
        info['file'] = inspect.getfile(obj)

    return info


if __name__ == "__main__":
    class MyClass:
        def __init__(self):
            self.attribute = "value"

        def method(self):
            pass


    def my_function():
        pass


    my_module = inspect

    obj1 = MyClass()
    obj2 = my_function

    print(introspection_info(obj1))
    print('*' * 30)
    print(introspection_info(obj2))
    print('*' * 30)
    print(introspection_info(my_module))
