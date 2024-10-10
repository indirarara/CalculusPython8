# Kalkulus

Kalkulus adalah alat yang sangat kuat untuk memahami dan menganalisis segala sesuatu yang berubah di sekitar kita. Dengan memahami konsep-konsep dasar seperti grafik fungsi, limit, kekontinuan, domain, range, dan trigonometri, kamu akan lebih siap untuk mempelajari kalkulus secara lebih mendalam. Proyek ini terdiri dari beberapa modul yang berfungsi untuk menganalisis berbagai karakteristik fungsi, seperti:

1. **Grafik Fungsi:** Menampilkan grafik fungsi untuk memvisualisasikan bentuk dan perilaku fungsi.
2. **Domain dan Range:** Menganalisis domain dan range dari fungsi untuk mengetahui batasan nilai input dan output.
3. **Kekontinuan:** Memeriksa apakah fungsi tersebut kontinu pada interval tertentu.
4. **Limit:** Menghitung limit fungsi di titik tertentu untuk mengetahui perilaku fungsi saat mendekati titik tersebut.
5. **Trigonometri:** Menghitung berbagai fungsi trigonometri dan sifat-sifatnya.
   
Proyek ini menggunakan pustaka **SymPy** untuk perhitungan simbolik dan **Matplotlib** untuk visualisasi grafik.

# FITUR UTAMA 

1. **Grafik Fungsi:** Memungkinkan pengguna untuk memvisualisasikan fungsi matematika dalam bentuk grafik untuk analisis lebih lanjut.
2. **Domain dan Range:** Menganalisis domain dan range dari fungsi untuk mengetahui input dan output yang valid dari fungsi tersebut.
3. **Kekontinuan:** Mengecek apakah fungsi kontinu di suatu titik atau pada interval tertentu.
4. **Limit:** Menghitung limit fungsi saat mendekati titik tertentu dari sisi kiri dan kanan.
5. **Trigonometri:** Menghitung berbagai nilai fungsi trigonometri seperti sinus, cosinus, dan tangen.

# CARA PENGGUNAAN 

1. **Install Python:** Pastikan Anda memiliki Python versi 3.x. Anda dapat mengunduh Python dari situs resmi Python.
2. **Install Project:** Jalankan **pip install CalculusPython8** di terminal.
   
```bash
pip install CalculusPython8
```

3. **Jika ingin menjalankan modul mencari grafik:**
   
```python
from grafik_fungsi.module_grafik import create_plot
create_plot((0, 2 * np.pi), np.sin)
```
4. **Jika ingin menjalankan modul mencari domain dan range:**
   
```python
from domain_range.module_domain_dan_range import analisis_fungsi
domain, f_range = analisis_fungsi("x**2")
```
5. **Jika ingin menjalankan modul mencari kontinu:**
   
```python
from kekontinuan.module_kekontinuan import is_continuous, check_continuity_interval, check_continuity_at_points, is_continuous_everywhere
print(is_continuous(lambda x: x**2, 1))

print(check_continuity_interval(lambda x: 1/x if x != 0 else None, -1, 1))

points_to_check = [-1, 0, 1, 2]
print(check_continuity_at_points(lambda x: 1/x if x != 0 else None, points_to_check))

print(is_continuous_everywhere(lambda x: x**2, (-10, 10)))
```
6. **Jika ingin menjalankan modul mencari limit kanan dan kiri:**

 ```python
from limit.module_limit import hitung_limit_kanan_kiri
fungsi_str = '(x-2)/(x+3) jika x<1, x**2 + 3*x jika x>=1'
titik = 1
```

7. **Jika ingin menjalankan modul mencari trigonometri:**
   
 ```python
from trigonometri.module_trigonometri import hitung_trigonometri_dengan_kuadran
hitung_trigonometri_dengan_kuadran(30, 2)
```

## Tentang Modul

