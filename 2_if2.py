"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def compare_strings(string_1, string_2):
    if isinstance(string_1, str) and isinstance(string_2, str):
        if string_1 == string_2:
            return 1
        if len(string_1) > len(string_2):
            return 2
        if string_2 == 'learn':
            return 3
    return 0


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    print(compare_strings('string', 5))
    print(compare_strings('string', 'string'))
    print(compare_strings('longer string', 'string'))
    print(compare_strings('str', 'learn'))


if __name__ == "__main__":
    main()
