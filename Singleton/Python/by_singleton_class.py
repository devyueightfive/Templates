class BadSingleton:
    # static variable
    value = 0


class ClassicSingleton(object):
    def __new__(cls):
        if not hasattr(cls, 'value'):
            cls.value = super().__new__(cls)
        return cls.value


def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


@singleton
class MyClass:
    pass


def check_BadSingleton():
    BadSingleton.value = 1
    BadSingleton.another_value = 2
    instance = BadSingleton()
    print('Class.v = ', BadSingleton.value)
    print('instance.v = ', instance.value)
    print("\nClass update")
    BadSingleton.value = 2
    print('Class.v = ', BadSingleton.value)
    print('instance.v = ', instance.value)
    print("\nInstance update")
    instance.value = 3
    print('Class.v = ', BadSingleton.value)
    print('instance.v = ', instance.value)
    second_instance = BadSingleton()
    print('second_instance.v = ', second_instance.value)
    print("\nClass update")
    BadSingleton.value = 4
    print('Class.v = ', BadSingleton.value)
    print('instance.v = ', instance.value)
    print('second_instance.v = ', second_instance.value)


def check_MyClass():
    instance = MyClass()
    instance.value = 0
    print('instance.v = ', instance.value)
    second_instance = MyClass()
    print('second_instance.v = ', second_instance.value)
    print("\nInstance update")
    instance.value = 3
    print('instance.v = ', instance.value)
    print('second_instance.v = ', second_instance.value)
    third_instance = MyClass()
    print('third_instance.v = ', third_instance.value)
    print("\nInstance update")
    third_instance.value = 5
    print('instance.v = ', instance.value)
    print('second_instance.v = ', second_instance.value)
    print('third_instance.v = ', third_instance.value)
    print('\nAdd attr another_value:')
    third_instance.another_value = 10
    print('instance.another_value = ', instance.another_value)
    print('second_instance.another_value = ', second_instance.another_value)
    print('third_instance.another_value = ', third_instance.another_value)


if __name__ == "__main__":
    # check_MyClass()
    check_BadSingleton()
