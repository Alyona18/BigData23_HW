# создает бинарный файл (min 2Гб), состоящий из случайных 32-разрядных беззнаковых целых чисел (big endian)
from random import randint
import struct

def create(f_name, n):
    with open(f_name, 'wb') as out:
        for i in range(n):
            num = randint(0, 2**32-1)
            out.write(struct.pack('>I', num))
    out.close()