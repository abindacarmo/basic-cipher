import math

ciphertext = "DFAOTASTRUEAOCIIYILPOIHGSAAESEISCTASCHLEWTTAACEINTTTVRITAUTBDEANMGNLDSAOHHEONVALNEUEHEFVEEITTSPATYH"
key = "EDUCATION"

cols = len(key)
rows = len(ciphertext) // cols

# urutan kolom
order = sorted(list(enumerate(key)), key=lambda x: x[1])

# buat matrix kosong
matrix = [[""] * cols for _ in range(rows)]

index = 0

# isi kolom sesuai urutan alphabet key
for i, (original_pos, _) in enumerate(order):
    for r in range(rows):
        matrix[r][original_pos] = ciphertext[index]
        index += 1

# baca row-wise
plaintext = ""
for r in range(rows):
    for c in range(cols):
        plaintext += matrix[r][c]

print("Plaintext:", plaintext)