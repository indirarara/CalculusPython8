import sympy as sp

def hitung_limit_kanan_kiri(fungsi_str, titik):
    
    x = sp.Symbol('x') 
    fungsi_kondisi_list = fungsi_str.split(',')
    kondisi_pieces = []

    for fungsi_kondisi in fungsi_kondisi_list:

        if "jika" in fungsi_kondisi:
            fungsi_part, kondisi_part = fungsi_kondisi.split("jika")
            fungsi = sp.sympify(fungsi_part.strip())
            kondisi = sp.sympify(kondisi_part.strip())
            kondisi_pieces.append((fungsi, kondisi))
        else:

            fungsi = sp.sympify(fungsi_kondisi.strip())
            kondisi_pieces.append((fungsi, True))

    fungsi_piecewise = sp.Piecewise(*kondisi_pieces)
    limit_kanan = sp.limit(fungsi_piecewise, x, titik, dir='+')
    limit_kiri = sp.limit(fungsi_piecewise, x, titik, dir='-')
    
    return limit_kanan, limit_kiri



# contoh penggunaan
# fungsi_str = '(x-2)/(x+3) jika x<1, x**2 + 3*x jika x>=1'
# titik = 1
# limit_kanan, limit_kiri = hitung_limit_kanan_kiri(fungsi_str, titik)

# print(f"Limit kanan dari f(x) ketika x mendekati {titik} adalah {limit_kanan}")
# print(f"Limit kiri dari f(x) ketika x mendekati {titik} adalah {limit_kiri}")