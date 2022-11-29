import cvxpy as cp

# 決定変数を定義
x1, x2 = cp.Variable(), cp.Variable()
# 目的関数を記述
obj = cp.Maximize(20 * x1 + 60 * x2)
# 制約の記述
cons = [
    5 * x1 + 4 * x2 <= 80,
    2 * x1 + 4 * x2 <= 40,
    2 * x2 + 8 * x2 <= 64,
    x1 >= 0,
    x2 >= 0,
]

# 最適化問題を定義
P = cp.Problem(obj, cons)
P.solve(verbose=True)
print(x1.value, x2.value)
