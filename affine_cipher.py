# AFFINE CIPHER DECRYPTION

ciphertext = "UFQFAU OMF FNDO VNEE"

# Key from frequency analysis
a = 11
b = 13

# Modular inverse of 11 mod 26
a_inv = 19

def char_to_num(c):
    return ord(c) - ord('A')

def num_to_char(n):
    return chr(n + ord('A'))

plaintext = ""

for char in ciphertext:

    if char.isalpha():

        y = char_to_num(char)

        # formula Affine decryption
        x = (a_inv * (y - b)) % 26

        plaintext += num_to_char(x)

    else:
        plaintext += char

print("Ciphertext :", ciphertext)
print("Plaintext  :", plaintext)