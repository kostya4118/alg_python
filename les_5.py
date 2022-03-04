import hashlib

def is_eq_str(a: str, b: str, verbose=False) -> bool:
    assert len(a) > 0 and len(b) > 0, 'Строки не могут быть пустыми!'

    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    if verbose:
        print(f'hash 1 - {ha}\nhash 2 - {hb}')

    return ha == hb

def Rabin_Karp(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустыми!'
    assert len(s) >= len(subs), 'Подстрока длиннее строки!'

    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len(subs) + 1):
        if h_subs == hashlib.sha1(s[i:i + len(subs)].encode('utf-8')).hexdigest():
            if subs == s[i:i + len(subs)]:
                return i
    return -1


# s1 = input('Введите строку 1: ')
# s2 = input('Введите строку 2: ')
# print('Строки одинаковые' if is_eq_str(s1, s2, True) else 'Строки разные')

s1 = input('Введите строку: ')
s2 = input('Введите подстроку: ')
pos = Rabin_Karp(s1, s2)
print(f'Подстрока найдена в позиции {pos}' if pos != -1 else 'Подстрока не найдена')