import string

numeros = string.digits
minus = string.ascii_lowercase
majus = string.ascii_uppercase
simbols = r"""!,"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"""

def comb_to_password(long, charset, password):
    # Validación
    if len(password) != long:
        raise ValueError("La longitud no coincide con la contraseña dada")

    base = len(charset)  # tamaño del conjunto de caracteres
    total = 0

    # Convertimos la contraseña a un "número" en base 'base'
    for i, char in enumerate(password):
        pos = charset.index(char)
        exponente = long - i - 1
        total += pos * (base ** exponente)

    # Sumamos 1 porque contamos también la combinación final (la contraseña misma)
    return total + 1


# === Ejemplo de uso ===
charset = minus + majus + numeros + simbols
password = "xT&4"
long = 4

resultado = comb_to_password(long, charset, password)
print(f" {resultado} combinaciones per arribar a '{password}'.")
