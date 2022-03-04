"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача
считается не решённой.
"""

import hashlib

def get_count_subs(s):
    assert len(s) > 0,  'Строка не может быть пустой'
    __hashs = []
    for i in range(len(s)):
        for j in range(i, len(s)):
             if len(s) != len(s[i:j+1]):
                __hash = hashlib.sha1(s[i:j+1].encode('utf-8')).hexdigest()
                if __hash not in __hashs:
                    __hashs.append(__hash)
    return len(__hashs)


s = input('Введите строку: ')
print(f'Строка {s} содержит {get_count_subs(s)} различающихся подстрок')
