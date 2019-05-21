from polynomial import get_polynomial


def bisection(begin_of_interval, end_of_interval):

    middle_of_interval = begin_of_interval
    amount_of_iterations = 0

    while (end_of_interval - begin_of_interval) >= 0.00001:

        # інкрементуємо кількість ітерацій
        amount_of_iterations += 1

        print("Інтерація %d" % amount_of_iterations)
        print("Початок інтервалу: %.6f" % begin_of_interval)
        print("Кінець інтервалу: %.6f" % end_of_interval)
        print("Значення функції на початку інтервалу: %.6f" % get_polynomial(begin_of_interval))
        print("Значення функції на кінці інтервалу: %.6f \n" % get_polynomial(end_of_interval))

        # знаходимо середину інтервалу
        middle_of_interval = (begin_of_interval + end_of_interval) / 2

        # перевірка чи середина інтервалу є кореном поліному
        if abs(get_polynomial(middle_of_interval)) <= 0.00001:
            break

        # визначаємо межу інтервалу і повторюємо шаги
        if get_polynomial(middle_of_interval) * get_polynomial(begin_of_interval) < 0:
            end_of_interval = middle_of_interval
        else:
            begin_of_interval = middle_of_interval

    print("Значення кореня рівння є : ", "%.6f\n" % middle_of_interval)
    print("Кількість ітерацій є: %d" % amount_of_iterations)


# bisection(-3, -2)
bisection(4, 5)
