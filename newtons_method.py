from polynomial import get_polynomial, get_polynomial_derivative


def newton(begin_of_interval, end_of_interval):

    amount_of_iterations = 0

    # початковим значення є початок інтервалу
    xn = begin_of_interval

    # ітеруємося по кожному значенню із заданого інтервалу
    for n in range(begin_of_interval, end_of_interval + 1):

        # інкрементуємо кількість ітерацій
        amount_of_iterations += 1

        # розраховую значення полінома у точці xn
        polynomial = get_polynomial(xn)

        print("Інтерація %d" % amount_of_iterations)
        print("Значення поточного наближення: %.6f" % xn)
        print("Значення функції у точці: %.6f\n" % get_polynomial(xn))

        # якщо значення полінома менше за встановлену точність, то зупиняю цикл
        if abs(polynomial) <= 0.00001:
            print("Значення кореня рівння є : ", "%.6f\n" % xn)
            print("Кількість ітерацій є: %d" % amount_of_iterations)
            break

        # якщо ні, то обчислюю значення похіодної полінома в точці хn
        polynomial_derivative = get_polynomial_derivative(xn)

        if polynomial_derivative == 0:
            print('Zero derivative. No solution found.')
            continue

        # обчислюю нове значення xn
        xn = xn - polynomial / polynomial_derivative

        print("Значення кореня рівння є : ", "%.6f\n" % xn)


#newton(-3, -2)
newton(4, 5)
