# name = 'Doni'
# age = None
# a = 37
# print(id(a))
# a = 'hello world!'
# print(id(a))

# res = input('you are: ')
# print('you wrote', res)
# age = int(input('how old u r?'))
# dat = [0,1,2,3,4]

# for item in dat:
#     print(item)
    
# count = 6
# for i in range(count):
#     for j in range(count):
#         for k in range(count):
#             print(i, j, k)    
            
# a = 5
# b = 'engine'
# print(type(a))
# print(bytes(a), id(b))
# print(hash(a))   
# help(str)  
# list = [1, 2.15, True, " we are "]
# print(list)
# list = []
# print(list)
# name = 'doni'
# age = 35
# text = 'I am %s and me %d!'% (name, age)
# print(text)
# text = 'I am {} and me {}!'.format (name, age)
# print(text)
# text = f'I am {name} and me {age}!'
# print(text)

# def my_func(n, data=[]):
#     for i in range(1, n+1):
#         data.append(i)
#     return data


# new_list = my_func(4)
# print(f'{new_list }')
# another_list = my_func(6)
# print(f'{another_list }')


# def my_func(n, data=None):
#     if data is None:
#         data = []
#     for i in range(1, n+1):
#           data.append(i)
#     return data


# new_list = my_func(4)
# print(f'{new_list }')
# another_list = my_func(6)
# print(f'{another_list }')

# print(chr(1875))

# print(ord('b'))
# a = 10
# b = 12
# a, b = b, a   # это значит перед и поселе = нужно одинаково колво элемент и они меняются местамы
# print(f'{a = }\t{b = }')

# data = [1, 2, 5, 10, 105, ]
# print(*data, sep='\t')  # это метод место for in item

# a = b = c = 0
# a += 15

# print(f'{a}, {b}, {c}')

# data = {1, 2, 3, 4, 5}
# a, b, *c, d = data
# print(a, b, c, d)

# list = [1, 2, 3, 4]
# list_new = iter(list)
# print(list_new)
# print(*list_new)
# print(*list_new)

# data = {'один': 1, 'two': 2, 'three': 3}
# x = iter(data.items())
# print(x)
# y = next(x)
# print(y)
# z = next(iter(y))
# print(z)


# list = [2, 5, 17, 16, 82, 91, 86]
# # res = [item for item in list if item % 2 == 0]
# # print(f'{res = }')
# res = {None: item for item in list if item > 4}
# res1 = (item for item in list if item > 4)
# res2 = [[item] for item in list if item > 4]
# print(res, res1, res2)

def gen(a: int, b: int):
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        yield int(i)
        #yoeld str(i) тоже можно входит как строковой 
for item in gen(10,1):
    print(f'{item = }')

