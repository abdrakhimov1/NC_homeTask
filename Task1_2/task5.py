# Написать функцию-параметрический декоратор fix_float(presision), который:
# 1) принимает один целочисленый аргумент - заданную точность;
# 2) заменяет все вещественные (как позиционные, так и именные)
# параметры произвольной декорируемой функции,
# а также её возвращаемое значение,
# округляя их до n-го знака после запятой,
# где n - заданная точность;
# 3) не вещественные параметры функции и возвращаемые значения не меняются.


def fix_float(presision):

    def a_decorator_passing_arguments(function_to_decorate):

        def a_wrapper_accepting_arguments(*args, **kwargs):

            def roundFunc(x):
                if type(x) == float:
                    return round(x, presision)
                else:
                    return x

            presisioned_args = [roundFunc(arg) for arg in args]
            presisioned_kwargs\
                = {key: roundFunc(val) for key, val in kwargs.items()}
            decorated_func\
                = function_to_decorate(*presisioned_args, **presisioned_kwargs)

            return roundFunc(decorated_func)

        return a_wrapper_accepting_arguments

    return a_decorator_passing_arguments


@fix_float(4)
def strange_multiplier(*args, mult=0):
    return sum(args) * args[mult]


print(strange_multiplier(
                            0.451235421901,
                            1.12312342121,
                            2.523412E-2,
                            4,
                            mult=-3
                            ))


@fix_float(2)
def add_greeting(greeting, number):
    return f'{greeting}, {number}!'


print(add_greeting('Hi', 10.4567))
