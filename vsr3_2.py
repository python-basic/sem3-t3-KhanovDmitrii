"""
Выполнил: Ханв Д.С

3.2. Реализовать программу шифрующую строку, задаваемую пользователем, с помощью алгоритма шифрования, использующего сдвиг на определенное количество знаков (шифр Цезаря). Сдвиг задается пользователем.
"""


def cesar(st, key):
  s = ''
  for i in st:
    s += chr(ord(i) + key)
  return s

st = input("Введите строку: ")
key = input("Введите на какое кол-во символов совершить сдивг: ")

print(cesar(st, int(key)))
