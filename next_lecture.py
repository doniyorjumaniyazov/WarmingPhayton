# f = open('my_text.txt')
# print(f)
# print(tuple(f))

# f = open('my_text.txt', 'a')
# f.write('get close\n')
# print(f)
# f.close()

# with (
#     open('my_text.txt', 'r+', encoding='utf-8') as f1, 
#     open('bin_data', 'rb') as f2, 
#     open('data_txt', 'r', encoding='utf-8', errors='makeagain') as f3
# ):
#         print(list(f1))
#         print(list(f2))
#         print(list(f3))   
# start = 10
# stop = 100
# with open('data.bin', 'bw+') as f:
#     for i in range(start, stop + 1):
#         f.write(str(i).encode('utf-8'))
#         if i % 3 == 0:
#             f.seek(-2, 1)
#     f.truncate(stop)
#     f.seek(0)
#     res = f.read(start) 
#     print(res.decode('utf-8'))       
