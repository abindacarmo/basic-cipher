import math

def get_order(key):
    sorted_key = sorted(list(key))
    order = []

    for char in key:
        order.append(sorted_key.index(char) + 1)
        sorted_key[sorted_key.index(char)] = None

    return order


def encrypt_columnar(text, key):

    text = text.replace(" ", "").upper()
    cols = len(key)

    rows = math.ceil(len(text) / cols)

    # padding
    while len(text) < rows * cols:
        text += "X"

    # matrix
    matrix = []

    index = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(text[index])
            index += 1
        matrix.append(row)

    # column order
    order = get_order(key)

    ciphertext = ""

    for num in range(1, cols + 1):

        col = order.index(num)

        for r in range(rows):
            ciphertext += matrix[r][col]

    return ciphertext


# PLAINTEXT
plaintext = "MY NAME IS BRIGIDA CARMO FROM VIQUEQUE DISTRICT"

# FIRST ENCRYPTION
cipher1 = encrypt_columnar(plaintext, "EDUCATION")

# SECOND ENCRYPTION
cipher2 = encrypt_columnar(cipher1, "ECONOMICS")

print("First Cipher  :", cipher1)
print("Final Cipher  :", cipher2)