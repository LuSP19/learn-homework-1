"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

sales = [
    {
        'product': 'iPhone 12',
        'items_sold': [
            363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186
        ]
    },
    {
        'product': 'Xiaomi Mi11',
        'items_sold': [
            317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316
        ]
    },
    {
        'product': 'Samsung Galaxy 21',
        'items_sold': [
            343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247
        ]
    },
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    total_sales = 0
    product_count = 0

    for product_sales in sales:
        total_product_sales = sum(product_sales['items_sold'])
        average_product_sales = round(total_product_sales / 12)
        total_sales += total_product_sales
        product_count += 1
        print(f'{product_sales["product"]}:')
        print(f'\tСуммарные: {total_product_sales}')
        print(f'\tСредние: {average_product_sales}\n')

    average_sales = round(total_sales / 12 / product_count)

    print(f'Суммарные продажи всех товаров: {total_sales}')
    print(f'Средние продажи всех товаров: {average_sales}')


if __name__ == "__main__":
    main()
