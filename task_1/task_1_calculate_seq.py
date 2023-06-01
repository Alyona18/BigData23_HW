#Вторая считает сумму этих чисел (с применением длинной арифметики), находит минимальное и максимальное число.
import struct
import decimal
import time

def calculate_seq(fname):
    sum_numbers = decimal.Decimal(0)
    min_num = 0
    max_num = 0
    with open(fname, 'rb') as inp:
        while True:
            data = inp.read(4)
            if not data:
                break
            num = struct.unpack('>I', data)[0]
            sum_numbers += num
            if num > max_num: max_num = num
            if num < min_num: min_num = num

    print(f'Сумма чисел: {sum_numbers}')
    print(f'Минимальное число: {min_num}')
    print(f'Максимальное число: {max_num}')


#start = time.time()
#calculate_seq("D:/big-data-2023/alms-bd-2023-3cecad0d39f8/tasks/output.bin")
#end = time.time()
#print('Время расчета последовательно: ', end-start)