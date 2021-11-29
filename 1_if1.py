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
def sort_by_age(age):
    if age < 6:
        return "Ходит в детский сад"
    if age < 18:
        return "Учится в школе"
    if age < 24:
        return "Учится в ВУЗе"
    else:
        return "Работает"

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """       
    age = int(input("Введите полное количество лет: "))
    does_what = sort_by_age(age)
    print(does_what)

if __name__ == "__main__":
    main()
