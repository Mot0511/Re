from re import *

comp = compile('\+?\d+\s?\(?\d+\)?[\s?\-?\d*]*')
print(comp.findall('+7 (351) 765-43-21'))
print(comp.findall('+234 (234) 234-345-345'))
