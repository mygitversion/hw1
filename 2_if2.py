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

def compare_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0
    if len(str1) == len(str2):
        return 1
    if len(str1) > len(str2):
        return 2
    if len(str1) != len(str2) and str2 == 'learn':
        return 3
    return "Для таких строк номерной вывод в этом задании не предусмотрен."

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    input_list = [('df2a8d', 100), ('ввод строки1', 'ввод строки2'), ('longer string', \
                  'learn'), ('more', 'learn'), ('more', 'learning')]
    
    for string1, string2 in input_list:
        result = compare_strings(string1, string2)
        print(f'Сравниваем:\n {string1}\n {string2}')
        print('результат:', result)
        print()
    
if __name__ == "__main__":
    main()
