from random import randint
import struct
import mmap
import threading


def create_with_map(f_name):
    num_numbers = 52428800 
    chunk_size = 1024 * 1024 * 256 

    with open(f_name, 'wb') as f:
        f.truncate(num_numbers * 4)

    with open(f_name, 'r+b') as f:
        mm = mmap.mmap(f.fileno(), 0)
        def generate_numbers(start, end):
            for i in range(start, end):
                num = randint(0, 2**32-1)
                mm.seek(i * 4)
                mm.write(struct.pack('>I', num))

        threads = []
        for i in range(0, num_numbers, chunk_size):
            start = i
            end = min(i + chunk_size, num_numbers)
            t = threading.Thread(target=generate_numbers, args=(start, end))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        mm.close()
