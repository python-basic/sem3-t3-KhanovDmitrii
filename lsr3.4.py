"""
Выполнил Ханов Д.С

ИСР 3.4
 Реализовать программу шифрующую строку, задаваемую пользователем, с помощью алгоритма шифрования ROT13. Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории.
"""


def ROT13(log, key):
  s = ''
  for i in log:
    s += key[str(i)]
  return s

a = [chr(i) for i in range(97, 110) ]
s = {}
for i in range(110, 123):
    s.update({a[i-110] : chr(i)})
a = [chr(i) for i in range(110, 123) ]
for i in range(97, 110):
    s.update({a[i-97] : chr(i)})

ip = input()

print(ROT13(ip, s))
