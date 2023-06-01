import struct
import decimal
import mmap
import time
import threading

def calculate_map(f_name):
    with open(f_name, 'r+b') as f:
        mm = mmap.mmap(f.fileno(), 0)
        num_threads = 4
        chunk_size = len(mm) // num_threads

        results = []

        def process_chunk(start, end):
            sum_numbers = decimal.Decimal(0)
            min_num = 0
            max_num = 0
            for i in range(start, end, 4):
                data = mm[i:i+4]
                num = struct.unpack('>I', data)[0]
                sum_numbers += num
                if num < min_num:
                    min_num = num
                if num > max_num:
                    max_num = num

            results.append((sum_numbers, min_num, max_num))

        threads = []
        for i in range(num_threads):
            start = i * chunk_size
            end = start + chunk_size
            if i == num_threads - 1:
                end = len(mm)
            thread = threading.Thread(target=process_chunk, args=(start, end))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    sum_numbers = decimal.Decimal(0)
    min_num = results[0][1]
    max_num = results[0][2]
    for result in results:
        sum_numbers += result[0]
        if result[1] < min_num:
            min_num = result[1]
        if result[2] > max_num:
            max_num = result[2]

    print(f'Сумма чисел: {sum_numbers}')
    print(f'Минимальное число: {min_num}')
    print(f'Максимальное число: {max_num}')