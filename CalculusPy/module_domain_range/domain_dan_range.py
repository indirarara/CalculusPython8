import sympy as sp

def temukan_domain_dan_range(expr):
    x = sp.Symbol('x')
    
    if expr.is_constant():
        domain = sp.S.Reals
        f_range = sp.simplify(expr)
    else:
        domain = sp.calculus.util.continuous_domain(expr, x, sp.S.Reals)
        f_range = sp.calculus.util.function_range(expr, x, domain)
    
    return domain, f_range

"""Fungsi untuk pengguna yang ingin menggunakan kode ini"""
def analisis_fungsi(expression):
    try:
        expr = sp.sympify(expression)
        domain, f_range = temukan_domain_dan_range(expr)

        return domain, f_range

    except Exception as e:
        return f"Terjadi kesalahan: {e}"