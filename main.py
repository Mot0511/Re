from re import *

# comp = compile('(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
comp = compile('25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.', 'dghsghdfgh')
print(comp.findall('klsdfjglsdkgfjls djk 253.148.1.1 dfkaplsjgldfsk 955.544.415.1.1 kkldfg;sjgidfjg; 123.123.1.1 ofijsldkfgd;sflgkj k5lk6mlk'))


# comp = compile('\w+\@\w+[\.\w+]*')
# print(comp.findall('mail@mail.ru smolnikov_a@ru.itstep.org mail@yandex.ru mail@gmail.com'))

# comp = compile('\+?\d+\s?\(?\d+\)?[\s?\-?\d*]*')
# print(comp.findall('+7 (351) 765-43-21'))
# print(comp.findall('+234 (234) 234-345-345'))
