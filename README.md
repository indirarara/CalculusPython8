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
limit_kanan, limit_kiri = hitung_limit_kanan_kiri(fungsi_str, titik)

```

7. **Jika ingin menjalankan modul mencari trigonometri:**
   
 ```python
from trigonometri.module_trigonometri import hitung_trigonometri_dengan_kuadran
hitung_trigonometri_dengan_kuadran(30, 2)
```

## Tentang Modul
Paket Kalkulus terdiri dari beberapa modul:

### 1. module_grafik
Modul ini memungkinkan pengguna untuk memvisualisasikan fungsi matematika dalam bentuk grafik untuk analisis lebih lanjut.

`create_plot`
Fungsi ini digunakan untuk membuat grafik dari suatu fungsi matematis dalam rentang x yang diberikan. Grafik ini dapat digunakan untuk visualisasi hubungan antara variabel x dan nilai fungsi y.

## Parameter:
`x_range (tuple):` Sebuah tuple yang berisi dua nilai, yaitu batas awal dan batas akhir dari rentang sumbu x. Contoh: (0, 10) untuk rentang x dari 0 hingga 10.

`function (callable):` Fungsi yang menerima satu argumen (x) dan mengembalikan sebuah nilai. Fungsi ini akan digambarkan dalam grafik. Fungsi ini harus menerima parameter x dan menghasilkan nilai y sesuai dengan x. Misalnya, fungsi kuadrat f(x) = x^2.

## Contoh Penggunaan:

```python
create_plot((0, 2 * np.pi), np.sin)
```

## Output:

### 2. module_domain_dan_range
Modul ini menganalisis domain dan range dari fungsi untuk mengetahui input dan output yang valid dari fungsi tersebut.

`temukan_domain_dan_range(expr)`
Fungsi ini digunakan untuk membuat grafik dari suatu fungsi matematis dalam rentang x yang diberikan. Grafik ini dapat digunakan untuk visualisasi hubungan antara variabel x dan nilai fungsi y.

## Parameter:
`expr:` Parameter ini berisi ekspresi matematika yang akan dianalisis. Ini bisa berupa fungsi matematika yang ingin dicari domain dan rangenya. Misalnya, ekspresi seperti x**2 + 2*x + 1, 1/(x-1), atau sqrt(x). Ekspresi ini diwakili dalam bentuk objek SymPy (seperti x**2, sin(x), dll).

`analisis_fungsi(expression)`

## Parameter:
`expression:` Ini adalah ekspresi matematika dalam format string yang akan dianalisis. Sebagai contoh, jika ingin menganalisis fungsi x**2 - 4, maka inputnya bisa berupa string 'x**2 - 4'. Fungsi ini kemudian mengubah string tersebut menjadi ekspresi SymPy untuk analisis lebih lanjut.

## Contoh Penggunaan:

```python
domain, f_range = analisis_fungsi("x**2")
```

## Output:

### 3. module_kekontinuan
Modul ini mengecek apakah fungsi kontinu di suatu titik atau pada interval tertentu.

`is_continuous(f, x, epsilon=1e-7)`
Fungsi ini digunakan untuk memeriksa apakah suatu fungsi matematika 𝑓(𝑥) kontinu di titik tertentu 𝑥. Kekontinuan di titik 𝑥 berarti limit kiri dan limit kanan di titik tersebut harus ada dan sama dengan nilai fungsi di titik tersebut.

## Parameter:
`f:` Fungsi yang akan diuji kekontinuannya di titik tertentu x.
`x:` Titik di mana kekontinuan dari fungsi f akan diuji.
`epsilon (opsional):` Penjelasan: Batas toleransi untuk menghitung limit kiri dan limit kanan. Ini digunakan untuk menghindari kesalahan numerik kecil dalam perhitungan limit. Jika selisih antara limit kiri, limit kanan, dan nilai fungsi di titik x lebih kecil dari epsilon, maka fungsi dianggap kontinu di titik tersebut.

`check_continuity_interval(f, start, end, step=0.1, epsilon=1e-7)`
Fungsi ini memeriksa kontinuitas suatu fungsi 𝑓(𝑥) dalam interval [𝑠𝑡𝑎𝑟𝑡,𝑒𝑛𝑑] dengan langkah tertentu (step). Fungsi ini akan mengevaluasi kontinuitas fungsi pada titik-titik yang terletak pada interval tersebut dan memberikan daftar titik-titik di mana fungsi tidak kontinu.

## Parameter:
`f:` Fungsi matematika yang akan diuji (seperti pada fungsi `is_continuous`).
`start:` Titik awal dari interval di mana fungsi f akan diuji kontinuitasnya.
`end:` Titik akhir dari interval di mana fungsi f akan diuji kontinuitasnya.
`step (opsional):` Jarak antara titik-titik evaluasi dalam interval. Misalnya, jika start=0, end=1, dan step=0.1, maka titik yang diuji adalah 0, 0.1, 0.2, ... hingga 1. Makin kecil nilai step, makin halus pengecekannya, tetapi lebih memakan waktu.
`epsilon (opsional):` Toleransi untuk menghitung limit (seperti pada fungsi is_continuous)

`check_continuity_at_points(f, points, epsilon=1e-7)`
Fungsi ini memeriksa kontinuitas fungsi 𝑓(𝑥) di beberapa titik yang diberikan. Fungsi ini berguna jika kita hanya ingin mengevaluasi kontinuitas fungsi pada titik-titik tertentu, bukan di seluruh interval.

## Parameter:
`f:` Fungsi matematika yang akan diuji (seperti pada fungsi is_continuous).
`points:` Daftar titik-titik di mana kekontinuan fungsi f akan diuji.
`epsilon (opsional):` Toleransi untuk menghitung limit di titik-titik yang diberikan.

`is_continuous_everywhere(f, domain, epsilon=1e-7, step=0.1)`
Fungsi ini memeriksa apakah fungsi 
𝑓(𝑥) kontinu di seluruh domain yang diberikan. Domain ditentukan dalam bentuk tuple (𝑠𝑡𝑎𝑟𝑡,𝑒𝑛𝑑). Fungsi ini digunakan untuk mengevaluasi kontinuitas fungsi dalam rentang nilai 𝑥 yang luas.

## Parameter:
`f:` Fungsi matematika yang akan diuji (seperti pada fungsi is_continuous).
`domain:` Tuple yang berisi titik awal dan titik akhir domain di mana fungsi akan diuji kontinuitasnya.
`epsilon (opsional):` Toleransi untuk menghitung limit dalam evaluasi kontinu di seluruh domain.
`step (opsional):` Jarak antar titik evaluasi dalam domain. Jika step kecil, fungsi akan diuji di banyak titik dan akan memberikan hasil yang lebih akurat.


## Contoh Penggunaan:

```python
# Cek kekontinuan di satu titik
print(is_continuous(lambda x: x**2, 1))
```
## Output:

```python
# Cek kekontinuan pada interval [-1, 1] untuk fungsi 1/x
print(check_continuity_interval(lambda x: 1/x if x != 0 else None, -1, 1))
```
## Output:

```python
# Cek kekontinuan di beberapa titik
points_to_check = [-1, 0, 1, 2]
print(check_continuity_at_points(lambda x: 1/x if x != 0 else None, points_to_check))
```
## Output:

```python
# Cek kekontinuan di seluruh domain [-10, 10]
print(is_continuous_everywhere(lambda x: x**2, (-10, 10)))  # True
```

## Output:



