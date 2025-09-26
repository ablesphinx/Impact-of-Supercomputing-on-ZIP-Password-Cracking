import string

num = string.digits
lc = string.ascii_lowercase
UC = string.ascii_uppercase
sym = r"""!,"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"""

# config #
charset = 0
password = 'x'
long = 0
# ------ #

def comb_to_password(long, charset, password):
    if len(password) != long:
        raise ValueError("La longitud no coincide con la contraseña dada")

    base = len(charset)
    total = 0

    for i, char in enumerate(password):
        pos = charset.index(char)
        exponent = long - i - 1
        total += pos * (base ** exponent)

    return total + 1

result = comb_to_password(long, charset, password)
print(f" {result} needed tries to crack '{password}'.")