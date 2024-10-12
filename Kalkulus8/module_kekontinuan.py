def is_continuous(f, x, epsilon=1e-7):
    from sympy import limit, Symbol  
    x_sym = Symbol('x')
    try:
        limit_left = limit(f(x_sym), x_sym, x, dir='-')
        limit_right = limit(f(x_sym), x_sym, x, dir='+')
        f_value = f(x)       
        return abs(limit_left - limit_right) < epsilon and abs(limit_left - f_value) < epsilon

    except ZeroDivisionError:
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def check_continuity_interval(f, start, end, step=0.1, epsilon=1e-7):
    discontinuities = []
    x = start
    while x <= end:
        if not is_continuous(f, x, epsilon):
            discontinuities.append(x)
        x += step
    return discontinuities

def check_continuity_at_points(f, points, epsilon=1e-7):
    results = []
    for x in points:
        try:
            is_cont = is_continuous(f, x, epsilon)
            results.append((x, is_cont))
        except Exception as e:
            print(f"Kesalahan saat mengecek titik {x}: {e}")
            results.append((x, False))
    
    return results

def is_continuous_everywhere(f, domain, epsilon=1e-7, step=0.1):
    start, end = domain
    x = start
    while x <= end:
        if not is_continuous(f, x, epsilon):
            return False
        x += step
    return True

# Cek kekontinuan di satu titik
# Menggunakan fungsi lambda sederhana untuk memeriksa kekontinuan pada x=1 untuk fungsi f(x) = x^2
# Output: True jika kontinu, False jika tidak
result = is_continuous(lambda x: x**2, 1)
print(f"Kontinuitas di x=1: {result}")  # True/False

# Cek kekontinuan pada interval [-1, 1] untuk fungsi 1/x
# Fungsi ini mengecek apakah ada diskontinuitas dalam interval [-1, 1] untuk f(x) = 1/x
# Output: Daftar titik di mana f(x) tidak kontinu
result_interval = check_continuity_interval(lambda x: 1/x if x != 0 else None, -2, 2)
print(f"Kontinuitas pada interval [-2, 2]: {result_interval}")

# Cek kekontinuan di beberapa titik
# Menggunakan lambda function f(x) = 1/x dan mengecek kekontinuan pada titik [-2, -1, 0, 1, 2]
# Output: Daftar tuple dengan setiap titik dan status kekontinuan (True/False)
points_to_check = [-2, -1, 0, 1, 2]
result_multiple_points = check_continuity_at_points(lambda x: 1/x if x != 0 else None, points_to_check)
print(f"Kontinuitas di beberapa titik: {result_multiple_points}")

# Cek kekontinuan di seluruh domain [-10, 10]
# Mengecek apakah fungsi f(x) = x^2 kontinu di seluruh interval [-10, 10]
# Output: True jika kontinu di seluruh interval, False jika ada diskontinuitas
result_everywhere = is_continuous_everywhere(lambda x: x**2, (-10, 10))
print(f"Kontinuitas di seluruh domain [-10, 10]: {result_everywhere}") #True or False
