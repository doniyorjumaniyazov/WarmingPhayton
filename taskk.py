# class User:
#     count = []
    
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
        
# u1 = User('One', '123-12')
# u2 = User('NoOne', '451-85-890')
# u1.count.append(42)
# u1.count.append(73)
# u2.counter = 256
# u2.count.append(u2.counter)
# u2.count.append(u1.count[-1])

# print(f'{u1.name = }, {u1.phone = }, {u1.count = }')        
# print(f'{u2.name = }, {u2.phone = }, {u2.count = }')
class A:
    name = 'A'
    
    def call(self):
       print(f'I am {self.name}')
       
class B:
    name = 'B'
    
    def call(self):
       print(f'I am {self.name}')
       
       
class C:
    name = 'C'
    
    def call(self):
       print(f'I am {self.name}')              
       
       
class D(C, A):
    pass

class E(D, B):
    pass

e = E()
e.call()
e.call()
       