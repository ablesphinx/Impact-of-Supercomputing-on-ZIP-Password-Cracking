import zipfile
import itertools
import string
import multiprocessing
import sys
from datetime import datetime
import os

num = string.digits
lc = string.ascii_lowercase
UC = string.ascii_uppercase
sym = r'''!,"#$%&'()*+,-./:;<=>?@[\]^_{|}~`'''

# config #
zip_path = 'x'
min_length = 0
max_length = 0
charset = 0
num_processes = 0
notify_every = 5000 #tries#
# ------ #

def try_password(zf_path, pwd):
    try:
        with zipfile.ZipFile(zf_path) as zf:
            zf.extractall(pwd=pwd.encode())
            return True
    except:
        return False

def worker(zf_path, prefix):
    pid = os.getpid()
    length = max_length
    remaining = length - len(prefix)
    counter = 0

    if remaining < 0:
        return None

    try:
        first = next(itertools.product(charset, repeat=remaining))
        print(f"[PID {pid}] Initialiting with prefix '{prefix}' -> First try: {prefix + ''.join(first)}")
    except StopIteration:
        return None

    for suffix in itertools.product(charset, repeat=remaining):
        pwd = prefix + ''.join(suffix)
        counter += 1

        if counter % notify_every == 0:
            print(f"[PID {pid}] Try #{counter}, last password: {pwd}")

        if try_password(zf_path, pwd):
            print(f"\n [PID {pid}] Password found: {pwd}")
            return pwd
    return None

def main():
    start = datetime.now()

    pool = multiprocessing.Pool(processes=num_processes)

    prefixes = [''.join(p) for p in itertools.product(charset, repeat=2)]

    tasks = [pool.apply_async(worker, (zip_path, prefix)) for prefix in prefixes]

    for task in tasks:
        result = task.get()
        if result:
            end = datetime.now()
            print(f"\n Contraseña correcta: {result}")
            print(f" Tiempo exacto: {end - start}")
            pool.terminate()
            sys.exit(0)

    print(" Contraseña no encontrada.")
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
