# 🔐 Classical Cipher Collection

Simple Python implementations of five classical ciphers, built for a cryptography exam (`Mid_Test`).

---

## Ciphers

**Hill Cipher** — `hill_cipher.py`  
Polygraphic substitution using matrix multiplication mod 26. Key must be an invertible n×n matrix.

**Affine Cipher** — `affine_cipher.py`  
Monoalphabetic substitution using:
```
E(x) = (a·x + b) mod 26
D(x) = a⁻¹·(x - b) mod 26
```
Key: pair (a, b) where gcd(a, 26) = 1.

**Double Columnar Transposition** — `double_columnar_transpozition.py`  
Applies columnar transposition twice. Characters are rearranged, not substituted.

**Keyword Columnar Transposition** — `keyword_columnar_transposition.py`  
Column order is determined by the alphabetical ranking of a keyword.

**Beaufort Cipher** — `beaufort.py`  
Reciprocal polyalphabetic cipher. Same operation for encrypt and decrypt:
```
C = (k - p) mod 26
```

---

## Run

```bash
python hill_cipher.py
python affine_cipher.py
python double_columnar_transpozition.py
python keyword_columnar_transposition.py
python beaufort.py
```

> No external dependencies — only Python's built-in `math` library.

---

## Author

**Brigida** · Informatics Engineering, UNTL · [@abindacarmo](https://github.com/abindacarmo)
