from polynomial import get_polynomial


def chord_method(begin_of_interval, end_of_interval):

    amount_of_iterations = 0

    # визначаємо значення с за формулою
    c = begin_of_interval

    # якщо значення поліному з коренем с більше 0.00001
    while abs(get_polynomial(c)) > 0.00001:

        c = (begin_of_interval * get_polynomial(end_of_interval) - end_of_interval * get_polynomial(begin_of_interval))\
            / (get_polynomial(end_of_interval) - get_polynomial(begin_of_interval))

        # інкрементуємо кількість ітерацій
        amount_of_iterations += 1

        print("Ітерація %d" % amount_of_iterations)
        print("Початок інтервалу: %.6f" % begin_of_interval)
        print("Кінець інтервалу: %.6f" % end_of_interval)
        print("Значення функції на початку інтервалу: %.6f" % get_polynomial(begin_of_interval))
        print("Значення функції на кінці інтервалу: %.6f \n" % get_polynomial(end_of_interval))

        # змінюємо значення с
        if get_polynomial(begin_of_interval) * get_polynomial(c) < 0:
            end_of_interval = c
        else:
            begin_of_interval = c

    print("Значення кореня рівння є : ", "%.6f\n" % c)
    print("Кількість ітерацій є: %d" % amount_of_iterations)


# chord_method(-3, -2)
chord_method(4, 5)
