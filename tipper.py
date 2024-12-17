from typing import Callable

def one_add_str(a: str):
    names = []
    def two_add_str(b: str):
        names.append(b)
        return a + ' , ' + ' , ' .join(names)
    
    return two_add_str

hello = one_add_str('Hello')
bye = one_add_str('Good bye')

print(hello('Doni'))
print(hello('Samiy'))
print(bye('Pari'))
print(hello('Suno'))
print(bye('Every one!'))