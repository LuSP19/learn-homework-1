"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def get_occupation(age):
    if 0 <= age < 7:
        return 'Учёба в детском саду'
    if 7 <= age < 18:
        return 'Учёба в школе'
    if 18 <= age < 23:
        return 'Учёба в ВУЗе'
    if age >= 23:
        return 'Работа'
    else:
        raise ValueError('Введён некорректный возраст')


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    age = int(input('Введите возраст: '))
    occupation = get_occupation(age)
    print(occupation)


if __name__ == "__main__":
    main()
