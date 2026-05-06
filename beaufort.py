# iha ne'e ita mak sei prense plaintext no nia keyword mak "STUDENT"


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def beaufort_encrypt(plaintext, key):

    plaintext = plaintext.upper()
    key = key.upper()

    # halo key naruk to plaintext nia naruk
    full_key = ""

    for i in range(len(plaintext)):
        full_key += key[i % len(key)]

    print("Plaintext :", plaintext)
    print("Key       :", full_key)
    print()

    ciphertext = ""

    for i in range(len(plaintext)):

        # foti valor letra
        p = alphabet.index(plaintext[i])
        k = alphabet.index(full_key[i])

        # formulario Beaufort
        c = (k - p) % 26

        # muda ba letra
        cipher_letter = alphabet[c]

        ciphertext += cipher_letter

        # fo sai prosesu
        print("STEP", i + 1)
        print("Plaintext :", plaintext[i], "=", p)
        print("Key       :", full_key[i], "=", k)

        print("Formula   : (" + str(k) + " - " + str(p) + ") % 26")
        print("          : (" + str(k - p) + ") % 26")
        print("          :", c)

        print("Cipher    :", cipher_letter)
        print("-" * 30)

    return ciphertext

result = beaufort_encrypt(input("Prense Plaintext: "), "STUDENT")

print()
print("Final Ciphertext :", result)



def beaufort_decrypt(ciphertext, key):

    ciphertext = ciphertext.upper()
    key = key.upper()

    # halo key sepanjang ciphertext
    full_key = ""

    for i in range(len(ciphertext)):
        full_key += key[i % len(key)]

    print("Ciphertext :", ciphertext)
    print("Key        :", full_key)
    print()

    plaintext = ""

    for i in range(len(ciphertext)):

        # foti valor letra
        c = alphabet.index(ciphertext[i])
        k = alphabet.index(full_key[i])

        # formula Beaufort Decrypt
        p = (k - c) % 26

        # troka ba letra
        plain_letter = alphabet[p]

        plaintext += plain_letter

        # fo sai prosesu
        print("STEP", i + 1)
        print("Ciphertext :", ciphertext[i], "=", c)
        print("Key        :", full_key[i], "=", k)

        print("Formula    : (" + str(k) + " - " + str(c) + ") % 26")
        print("           : (" + str(k - c) + ") % 26")
        print("           :", p)

        print("Plaintext  :", plain_letter)
        print("-" * 30)

    return plaintext





print("===========DEcrypt===========")


# Decrypt
plain = beaufort_decrypt(result, "STUDENT")
print("Plaintext  :", plain)



