# Написать генератор-декоратор(!) stat_counter,
# который конструирует объекты (назовём пока statistic), такие что:
# - первый вызов next(statistic) (он же statistic.send(None))
# возвращает словарь, в котором stat будет хранить информацию вида
# { функция: количество вызовов }, где функция
# — это исходный (не обёрнутый) объект-функция.
# - все последующие вызовы statistic.send(function)
# оборачивают вызов произвольной функции
# function увеличением на 1 соответствующего элемента словаря.
# Глобальными именами пользоваться нельзя

# ¯\_(ツ)_/¯

from collections import defaultdict


def stat_counter():

    func_number_of_calls = defaultdict(int)
    func = yield func_number_of_calls

    while True:
        def a_decorator_passing_arguments(func):
            def a_wrapper_accepting_arguments(*args, **kwargs):
                func_number_of_calls[func] += 1
                return func(*args, **kwargs)
            return a_wrapper_accepting_arguments
        func = yield a_decorator_passing_arguments(func)


statistic = stat_counter()
function_calls_statistic = next(statistic)

print(function_calls_statistic)


@statistic.send
def test_function_1():
    print('First function worked well')
    return 0


@statistic.send
def test_function_2():
    test_function_1()
    test_function_1()
    print('Second function worked well')
    return 0


@statistic.send
def test_function_3():
    test_function_1()
    test_function_1()
    test_function_2()
    test_function_2()
    print('Third function worked well')
    return 0


test_function_1()
test_function_2()
test_function_3()

print(function_calls_statistic)
