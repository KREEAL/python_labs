# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# все двузначные которые равны удвоенному произведению своих цифр
# все трехзначные числа, квадрат которых оканчивается цифрами равными самому числу
# все трехзначные, сумма цифр которых равна заданному числу n
# из диапазона от А до B вывести четырехзначные числа, являющиеся палиндромом
# из диапазона от А до B вывести четырехзначные числа, содержащие ровно три одинаковые цифры
def sum_cifr(number):
    acc = 0
    while number > 0:
        acc += (number % 10)
        number = int(number / 10)
    return acc


def is_palindrome_number(number):
    new_st = str(number)
    return new_st == new_st[::-1]


def is_have_three_digits(number):
    list_n = list(str(number))
    for i in range(0, 10):
        if list_n.count(str(i)) == 3:
            return True
    return False


def first_task():
    print('Первая задача:')
    for i in range(10, 100):
        if i == 2 * (i % 10) * ((i - i % 10) / 10):
            print(i)
    print()


def second_task():
    print('Вторая задача')
    for i in range(100, 1000):
        if ((i ** 2) % 1000) == i:
            print(i)
    print()


def third_task():
    print('Третья задача')
    n = int(input('Введите n '))
    for i in range(100, 1000):
        if (sum_cifr(i) == n):
            print(i)
    print()


def fourth_task():
    print('Четвертая задача')
    a, b = map(int, input('Введите А и В ').split())
    for i in range(a, b + 1):
        if i >= 1000 and i <= 9999:
            if (is_palindrome_number(i)):
                print(i)
    print()


def fifth_task():
    print('Пятая задача')
    a, b = map(int, input('Введите А и В ').split())
    for i in range(a, b + 1):
        if 1000 <= i <= 9999:
            if is_have_three_digits(i):
                print(i)
    print()


def main():
    first_task()
    second_task()
    third_task()
    fourth_task()
    fifth_task()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
