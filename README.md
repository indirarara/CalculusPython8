# KALKULUS

Kalkulus adalah alat yang sangat kuat untuk memahami dan menganalisis segala sesuatu yang berubah di sekitar kita. Dengan memahami konsep-konsep dasar seperti grafik fungsi, limit, kekontinuan, domain, range, dan trigonometri, kamu akan lebih siap untuk mempelajari kalkulus secara lebih mendalam. Proyek ini terdiri dari beberapa modul yang berfungsi untuk menganalisis berbagai karakteristik fungsi, seperti:

1. **Grafik Fungsi:** Menampilkan grafik fungsi untuk memvisualisasikan bentuk dan perilaku fungsi.
2. **Domain dan Range:** Menganalisis domain dan range dari fungsi untuk mengetahui batasan nilai input dan output.
3. **Kekontinuan:** Memeriksa apakah fungsi tersebut kontinu pada interval tertentu.
4. **Limit:** Menghitung limit fungsi di titik tertentu untuk mengetahui perilaku fungsi saat mendekati titik tersebut.
5. **Trigonometri:** Menghitung berbagai fungsi trigonometri dan sifat-sifatnya.
   

# FITUR UTAMA 

1. **Grafik Fungsi:** Memungkinkan pengguna untuk memvisualisasikan fungsi matematika dalam bentuk grafik untuk analisis lebih lanjut.
2. **Domain dan Range:** Menganalisis domain dan range dari fungsi untuk mengetahui input dan output yang valid dari fungsi tersebut.
3. **Kekontinuan:** Mengecek apakah fungsi kontinu di suatu titik atau pada interval tertentu.
4. **Limit:** Menghitung limit fungsi saat mendekati titik tertentu dari sisi kiri dan kanan.
5. **Trigonometri:** Menghitung berbagai nilai fungsi trigonometri seperti sinus, cosinus, dan tangen.

# CARA PENGGUNAAN 

1. **Install Project:** Jalankan **pip install Kalkulus8** di terminal.
   
```bash
pip install Kalkulus8
```

2. **Jika ingin menjalankan modul yang ada di Kalkulus8:**
   
```bash
from Kalkulus8 import *
```

3. **Panggil fungsi yang ingin Anda gunakan:**

   ***Contoh Pemanggilan:***
   
```python
# Modul Grafik
import numpy as np
create_plot((0, 2 * np.pi), np.sin)

# Modul Domain dan Range
hasil = analisis_fungsi("sqrt(49)")  
print(hasil)

# Modul Kekontinuan
hasil = is_continuous(lambda x: x**2, 1)
print(f"Kontinuitas di x=1: {hasil}")

hasil = check_continuity_interval(lambda x: 1/x if x != 0 else None, -2, 2)
print(f"Kontinuitas pada interval [-2, 2]: {hasil}")

titik = [-2, -1, 0, 1, 2]
hasil = check_continuity_at_points(lambda x: 1/x if x != 0 else None, titik)
print(f"Kontinuitas di beberapa titik: {hasil}")

hasil = is_continuous_everywhere(lambda x: x**2, (-10, 10))
print(f"Kontinuitas di seluruh domain [-10, 10]: {hasil}")

# Modul Limit
hasil = hitung_limit_kanan_kiri("x**2 jika x < 2, 3*x jika x >= 2", 2)
print(hasil)

# Modul Trigonometri
hasil = hitung_trigonometri_dengan_kuadran(45, 2) 
print(hasil)
```

## Tentang Modul
Paket Kalkulus terdiri dari beberapa modul:

### 1. module_grafik
Modul ini memungkinkan pengguna untuk memvisualisasikan fungsi matematika dalam bentuk grafik untuk analisis lebih lanjut.

a. `create_plot`

Fungsi ini digunakan untuk membuat grafik dari suatu fungsi matematis dalam rentang x yang diberikan. Grafik ini dapat digunakan untuk visualisasi hubungan antara variabel x dan nilai fungsi y.

**Parameter:**

* `x_range (tuple):` Sebuah tuple yang berisi dua nilai, yaitu batas awal dan batas akhir dari rentang sumbu x. Contoh: (0, 10) untuk rentang x dari 0 hingga 10.

* `function (callable):` Fungsi yang menerima satu argumen (x) dan mengembalikan sebuah nilai. Fungsi ini akan digambarkan dalam grafik. Fungsi ini harus menerima parameter x dan menghasilkan nilai y sesuai dengan x. Misalnya, fungsi kuadrat f(x) = x^2.

## Contoh Penggunaan:

```python
import numpy as np
create_plot((0, 2 * np.pi), np.sin)
```

## Output:

```python
grafik dari fungsi tersebut
```

### 2. module_domain_dan_range
Modul ini menganalisis domain dan range dari fungsi untuk mengetahui input dan output yang valid dari fungsi tersebut.

a. `validasi_input(expression):`

Fungsi ini digunakan untuk memvalidasi input atau ekspresi matematika yang diberikan.

**Parameter:**

* `expression:` Parameter ini berisi ekspresi matematika yang akan dianalisis. Ini bisa berupa fungsi matematika yang ingin dicari domain dan rangenya. Misalnya, ekspresi seperti x ** 2 + 2 * x + 1, 1/(x-1), atau sqrt (x). Ekspresi ini diwakili dalam bentuk objek SymPy (seperti x ** 2, sin (x), dll).


b. `temukan_domain_dan_range(expression)`

Fungsi ini digunakan untuk menemukan domain dan range dari suatu ekspresi matematika.

**Parameter:**

* `expression:` Parameter ini berisi ekspresi matematika yang akan dianalisis. Ini bisa berupa fungsi matematika yang ingin dicari domain dan rangenya. Misalnya, ekspresi seperti x ** 2 + 2 * x + 1, 1/(x-1), atau sqrt (x). Ekspresi ini diwakili dalam bentuk objek SymPy (seperti x ** 2, sin (x), dll).


c. `analisis_fungsi(expression)`

Fungsi ini adalah fungsi yang menerima ekspresi matematika dalam bentuk string dan kemudian memanggil fungsi `temukan_domain_dan_range()` untuk menganalisis domain dan range dari ekspresi tersebut.

**Parameter:**

* `expression:`  Parameter ini berisi ekspresi matematika yang akan dianalisis. Ini bisa berupa fungsi matematika yang ingin dicari domain dan rangenya. Misalnya, ekspresi seperti x ** 2 + 2 * x + 1, 1/(x-1), atau sqrt (x). Ekspresi ini diwakili dalam bentuk objek SymPy (seperti x ** 2, sin (x), dll).

## Contoh Penggunaan:

```python
hasil = analisis_fungsi("sqrt(49)")  
print(hasil)
```

## Output:

```python
Semua bilangan real, Range: {7}
```


### 3. module_kekontinuan

Modul ini mengecek apakah fungsi kontinu di suatu titik atau pada interval tertentu.

a. `is_continuous(f, x, epsilon=1e-7)`

Fungsi ini digunakan untuk memeriksa apakah suatu fungsi matematika 𝑓(𝑥) kontinu di titik tertentu 𝑥. Kekontinuan di titik 𝑥 berarti limit kiri dan limit kanan di titik tersebut harus ada dan sama dengan nilai fungsi di titik tersebut.

**Parameter:**

* `f:` Fungsi yang akan diuji kekontinuannya di titik tertentu x.
* `x:` Titik di mana kekontinuan dari fungsi f akan diuji.
* `epsilon (opsional):` Batas toleransi untuk menghitung limit kiri dan limit kanan. Ini digunakan untuk menghindari kesalahan numerik kecil dalam perhitungan limit. Jika selisih antara limit kiri, limit kanan, dan nilai fungsi di titik x lebih kecil dari epsilon, maka fungsi dianggap kontinu di titik tersebut.

b. `check_continuity_interval(f, start, end, step=0.1, epsilon=1e-7)`

Fungsi ini memeriksa kontinuitas suatu fungsi 𝑓(𝑥) dalam interval [𝑠𝑡𝑎𝑟𝑡,𝑒𝑛𝑑] dengan langkah tertentu (step). Fungsi ini akan mengevaluasi kontinuitas fungsi pada titik-titik yang terletak pada interval tersebut dan memberikan daftar titik-titik di mana fungsi tidak kontinu.

**Parameter:**

* `f:` Fungsi matematika yang akan diuji (seperti pada fungsi `is_continuous`).
* `start:` Titik awal dari interval di mana fungsi f akan diuji kontinuitasnya.
* `end:` Titik akhir dari interval di mana fungsi f akan diuji kontinuitasnya.
* `step (opsional):` Jarak antara titik-titik evaluasi dalam interval. Misalnya, jika start=0, end=1, dan step=0.1, maka titik yang diuji adalah 0, 0.1, 0.2, ... hingga 1. Makin kecil nilai step, makin halus pengecekannya, tetapi lebih memakan waktu.
* `epsilon (opsional):` Toleransi untuk menghitung limit (seperti pada fungsi `is_continuous`)

c. `check_continuity_at_points(f, points, epsilon=1e-7)`
  
Fungsi ini memeriksa kontinuitas fungsi 𝑓(𝑥) di beberapa titik yang diberikan. Fungsi ini berguna jika kita hanya ingin mengevaluasi kontinuitas fungsi pada titik-titik tertentu, bukan di seluruh interval.

**Parameter:**

* `f:` Fungsi matematika yang akan diuji (seperti pada fungsi `is_continuous`).
* `points:` Daftar titik-titik di mana kekontinuan fungsi f akan diuji.
* `epsilon (opsional):` Toleransi untuk menghitung limit di titik-titik yang diberikan.

d. `is_continuous_everywhere(f, domain, epsilon=1e-7, step=0.1)`
  
Fungsi ini memeriksa apakah fungsi 𝑓(𝑥) kontinu di seluruh domain yang diberikan. Domain ditentukan dalam bentuk tuple (𝑠𝑡𝑎𝑟𝑡,𝑒𝑛𝑑). Fungsi ini digunakan untuk mengevaluasi kontinuitas fungsi dalam rentang nilai 𝑥 yang luas.

**Parameter:**

* `f:` Fungsi matematika yang akan diuji (seperti pada fungsi `is_continuous`).
* `domain:` Tuple yang berisi titik awal dan titik akhir domain di mana fungsi akan diuji kontinuitasnya.
* `epsilon (opsional):` Toleransi untuk menghitung limit dalam evaluasi kontinu di seluruh domain.
* `step (opsional):` Jarak antar titik evaluasi dalam domain. Jika step kecil, fungsi akan diuji di banyak titik dan akan memberikan hasil yang lebih akurat.


## Contoh Penggunaan:
a. `is_continuous`

```python
hasil = is_continuous(lambda x: x**2, 1)
print(f"Kontinuitas di x=1: {hasil}")
```

## Output:

```python
Kontinuitas di x=1: True
```

b. `check_continuity_interval`

```python
hasil = check_continuity_interval(lambda x: 1/x if x != 0 else None, -2, 2)
print(f"Kontinuitas pada interval [-2, 2]: {hasil}")
```
## Output:

```python
Kontinuitas pada interval [-2, 2]: []
```

c. `check_continuity_at_points`

```python
titik = [-2, -1, 0, 1, 2]
hasil = check_continuity_at_points(lambda x: 1/x if x != 0 else None, titik)
print(f"Kontinuitas di beberapa titik: {hasil}")
```
## Output:

```python
Kontinuitas di beberapa titik: [(-2, True), (-1, True), (0, False), (1, True), (2, True)]
```

d. `is_continuous_everywhere`

```python
hasil = is_continuous_everywhere(lambda x: x**2, (-10, 10))
print(f"Kontinuitas di seluruh domain [-10, 10]: {hasil}")
```

## Output:

```python
Kontinuitas di seluruh domain [-10, 10]: True
```

### 4. module_limit
Modul ini menghitung limit fungsi piecewise saat mendekati titik tertentu dari sisi kiri dan kanan.

a. `hitung_limit_kanan_kiri(fungsi_str, titik)`

Fungsi ini digunakan untuk menghitung batas (limit) kanan dan kiri dari suatu fungsi piecewise (fungsi yang terdefinisi dalam beberapa bagian atau kondisi yang berbeda) di sekitar titik tertentu. 

**Parameter:**

* `fungsi_str:` Ini adalah sebuah string yang menggambarkan fungsi piecewise dalam format tertentu. Fungsi ini dibagi oleh koma (,) antara bagian-bagian fungsi yang berbeda.Contoh "x** 2 jika x > 0, x ** 3 jika x <= 0".
* `titik:` Titik di mana limit kanan dan kiri akan dihitung. Titik ini adalah nilai dari 𝑥 yang digunakan dalam perhitungan limit fungsi piecewise.

## Contoh Penggunaan:

```python
hasil = hitung_limit_kanan_kiri("x**2 jika x < 2, 3*x jika x >= 2", 2)
print(hasil)
```
## Output:

```python
Limit kanan: 6
Limit kiri: 6
```

### 5. module_trigonometri
Modul ini menghitung berbagai nilai fungsi trigonometri seperti sinus, cosinus, dan tangen.

a. `trigonometri(sudut_derajat)`

Fungsi ini digunakan untuk menghitung nilai dari sinus (sin), kosinus (cos), tangen (tan), kosekan (cot), secans (sec), dan kosekan (csc) dari suatu sudut yang diberikan dalam satuan derajat.

**Parameter:**

* `sudut_derajat:` Sudut yang diberikan dalam satuan derajat.

b. `penyesualian_sudut_dengan_kuadran(sudut, kuadran)`
  
Fungsi ini digunakan untuk menyesuaikan nilai sudut agar sesuai dengan kuadran yang diberikan. 

**Parameter:**

* `sudut:` Sudut yang ingin disesuaikan dalam satuan derajat.
* `kuadran:` Kuadran tempat sudut berada (1-4).

c. `hitung_trigonometri_dengan_kuadran(sudut, kuadran)`
  
Fungsi ini menghitung nilai trigonometri untuk suatu sudut yang diberikan dengan mempertimbangkan kuadran yang sesuai.

**Parameter:**
* `sudut:` Sudut yang ingin disesuaikan dalam satuan derajat.
* `kuadran:` Kuadran tempat sudut berada (1-4).

## Contoh Penggunaan:

```python
Hasil = hitung_trigonometri_dengan_kuadran(45, 2) 
print(Hasil)
```
## Output:

```python
{'sudut asli': 45, 'sudut disesuaikan': 135, 'sin': 1, 'cos': -1, 'tan': -1, 'cot': -1, 'sec': -1, 'csc': 1}
```
