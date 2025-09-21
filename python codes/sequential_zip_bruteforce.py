import zipfile
import itertools
import string
from datetime import datetime

num = string.digits
lc = string.ascii_lowercase
UC = string.ascii_uppercase
sym = r'''!,"#$%&'()*+,-./:;<=>?@[\]^_{|}~`'''

# config #
zip_path = 'x'
min_length = 0
max_length = 0
charset = 0
# ------ #

def try_password(zf, pwd):
    try:
        zf.extractall(pwd=bytes(pwd, 'utf-8'))
        return True
    except:
        return False

def brute_force_zip(zip_path, min_length, max_length, charset, report_every=100000):
    tested = 0
    zf = zipfile.ZipFile(zip_path)
    start = datetime.now()

    for length in range(min_length, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            pwd = ''.join(attempt)
            tested += 1

            if tested % report_every == 0:
                elapsed = (datetime.now() - start).total_seconds()
                speed = tested / elapsed if elapsed > 0 else 0
                print(f"[{datetime.now().strftime('%H:%M:%S')}] {tested:,} passwords tried"
                      f"({speed:,.0f} per second)")

            if try_password(zf, pwd):
                print(f"\nPassword found: {pwd}")
                print(f"{tested:,} combinations tried")
                return start

    print("\nPassword not found in the specified range.")
    return None

if __name__ == '__main__':
    ahora = brute_force_zip(zip_path, min_length, max_length, charset)
    if ahora:
        tiempofloat = (datetime.now() - ahora).total_seconds()
        tiempostr = str(tiempofloat)
        print(tiempostr.replace(".",","))
