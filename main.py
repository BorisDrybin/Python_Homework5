'''RLE-сжатие – один из самых простых методов сжатия строки, основанный на сокращении подстрок, 
состоящих из одинаковых символов. Сжатие осуществляется следующим образом:
Строка разбивается на минимальное количество подстрок, состоящих из одинаковых символов. 
Например, abbcaaa превращается в строки a, bb, c, aaa.
Каждая из полученных строк превращается в строку, состоящую из числа и буквы. 
Числом является количество повторений символа в этой строке, буква берётся из первого символа обрабатываемой строки. 
Число не добавляется, если количество символов в строке равно единице. Из предыдущего массива строк мы получаем a, 2b, c, 3a.
Затем полученные строки конкатенируются в исходном порядке. В рассмотренном примере в итоге получим a2bc3a.
Вводится строка, нужно сжать ее по алгоритму, описанному выше.'''


# some_str = input('Введите строку: ')

# def rle_compress(some_str):
#     compressed = ''
#     prev_char = ''
#     count = 0

#     for char in some_str:
#         if char != prev_char:
#             if prev_char:
#                 compressed += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         compressed += str(count) + prev_char
#         return compressed
    
# compressed_str = rle_compress(some_str)
# print(compressed_str)



'''Создайте список из случайных чисел. Найдите номер его последнего локального 
максимума (локальный максимум — это элемент, который больше любого из своих соседей).'''


from random import randint
a = [randint(0, 10) for i in range(10)]
print(a)
a = [-1] + a + [-1]
for i in range(-2,-(len(a)),-1):
    if a[i - 1] < a[i] > a[i + 1]:
        print(f'Номер элемента: {(len(a) - 2)+(i + 1)} (нумерация с 0)')
        break