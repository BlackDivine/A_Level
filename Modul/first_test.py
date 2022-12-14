def spam(number):
    """Function should return something like this:
    spam(1);#bulochka
    spam(3);#bulochkabulochkabulochka
    But it is broken. Fix it please!

    Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    """
    return "bulochka" * number


def my_sum(list_of_numbers):

    """Function receives a list with integer numbers,
    :param list

    Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
    Не использовать встроенные функции суммирования.

    """

    if len(list_of_numbers) == 2:
        return list_of_numbers[0] + list_of_numbers[1]
    return list_of_numbers[0] + my_sum(list_of_numbers[1:])

    # suma = 0
    # for numbers in list_of_numbers:
    #     suma += int(numbers)          Cкучний варіант 
    # return suma
    #  ...wite your code here


def shortener(string):
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'


    """
    string = string.split()
    result_list = []
    for word in string:
        if len(word) > 6:
            result_list.append(word[:6] + "*")
        else:
            result_list.append(word)

    return " ".join(result_list)
    #  ...wite your code here


def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    return sum([1 for word in words if len(word) >= 2 and word[0] == word[-1]])
    #  ...wite your code here
