import zipfile
import itertools
import string
from datetime import datetime

numeros = string.digits
minus = string.ascii_lowercase
majus = string.ascii_uppercase
simbols = r'''!,"#$%&'()*+,-./:;<=>?@[\]^_{|}~`'''

# --- Configuració ---
zip_path = 'x'
min_length = 0
max_length = 0
charset = 0
# ---------------------

def try_password(zf, pwd):
    try:
        zf.extractall(pwd=bytes(pwd, 'utf-8'))
        return True
    except:
        return False

def brute_force_zip(zip_path, min_length, max_length, charset, report_every=100000):
    testeado = 0
    zf = zipfile.ZipFile(zip_path)
    start = datetime.now()

    for length in range(min_length, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            pwd = ''.join(attempt)
            testeado += 1

            if testeado % report_every == 0:  # CHIVATO
                elapsed = (datetime.now() - start).total_seconds()
                speed = testeado / elapsed if elapsed > 0 else 0
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Provades {testeado:,} contrasenyes "
                      f"({speed:,.0f} per segon)")

            if try_password(zf, pwd):
                print(f"\nContrasenya trobada: {pwd}")
                print(f"S'han provat {testeado:,} combinacions")
                return start

    print("\nContrasenya no trobada al rang especificat.")
    return None

if __name__ == '__main__':
    ahora = brute_force_zip(zip_path, min_length, max_length, charset)
    if ahora:
        tiempofloat = (datetime.now() - ahora).total_seconds()
        tiempostr = str(tiempofloat)
        print(tiempostr.replace(".",","))
