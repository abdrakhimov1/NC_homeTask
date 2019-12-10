# Ввести последовательность объектов Python (кортежей или целых чисел),
# и сымитировать работу Чудо-Конвейера.
# Если объект — кортеж, это означает,
# что на вход конвейеру подаются поочерёдно все объекты из этого кортежа.
# Если объект — натуральное число N, это означает,
# что с выхода конвейера надо снять поочерёдно N объектов,
# объединить их в кортеж и вывести. Если с конвейера нельзя снять N объектов,
# или в последовательности нет больше команд,
# Чудо-Конвейер немедленно останавливается.

lazyInput = ("QWE", 1.1, 234),\
            2, (None, 7), 0, 2,\
            (7, 7, 7), 2, (12, ),\
            (), 3, (5, 6), 3, 100500


def superConveer(anyInput):

    myConveer = []

    for elem in anyInput:

        if type(elem) == tuple:

            for each in elem:
                myConveer.append(each)

        else:
            if len(myConveer) == 0:
                return 0

            if len(myConveer) < elem:
                outSize = len(myConveer)

            else:
                outSize = elem

            print(tuple(myConveer.pop(0) for i in range(outSize)))

    if len(myConveer) == 0:
        return 0


superConveer(lazyInput)
