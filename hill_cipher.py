# HILL CIPHER DECRYPTION (CLASS A)

# Ciphertext
ciphertext = "JLPTJEVTVXNE"

# Key inverse matrix
K_inv = [
    [23, 22],
    [5, 19]
]

# Function: convert letter -> number
def char_to_num(c):
    return ord(c) - ord('A')

# Function: convert number -> letter
def num_to_char(n):
    return chr(n + ord('A'))

# Remove spaces and uppercase
ciphertext = ciphertext.upper().replace(" ", "")

plaintext = ""

# Process 2 letters at a time
for i in range(0, len(ciphertext), 2):

    # Take pair
    pair = ciphertext[i:i+2]

    # Convert to numbers
    c1 = char_to_num(pair[0])
    c2 = char_to_num(pair[1])

    # Matrix multiplication
    p1 = (K_inv[0][0] * c1 + K_inv[0][1] * c2) % 26
    p2 = (K_inv[1][0] * c1 + K_inv[1][1] * c2) % 26

    # Convert back to letters
    plaintext += num_to_char(p1)
    plaintext += num_to_char(p2)

    # Show process
    print(f"{pair} -> {num_to_char(p1)}{num_to_char(p2)}")

# Final plaintext
print("\nPlaintext :", plaintext)