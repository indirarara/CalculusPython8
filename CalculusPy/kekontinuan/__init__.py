# # Cek kekontinuan di satu titik
# print(is_continuous(lambda x: x**2, 1))  # True

# # Cek kekontinuan pada interval [-1, 1] untuk fungsi 1/x
# print(check_continuity_interval(lambda x: 1/x if x != 0 else None, -1, 1))

# # Cek kekontinuan di beberapa titik
# points_to_check = [-1, 0, 1, 2]
# print(check_continuity_at_points(lambda x: 1/x if x != 0 else None, points_to_check))

# # Cek kekontinuan di seluruh domain [-10, 10]
# print(is_continuous_everywhere(lambda x: x**2, (-10, 10)))  # True