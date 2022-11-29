import cvxpy as cp
import numpy as np

# ベクトル形式で決定変数を定義
x = cp.Variable(2)
c = np.array([20.0, 60.0])
# 制約はGx <= hで表す
G = np.array([[5.0, 4.0], [2.0, 4.0], [2.0, 8.0], [-1.0, 0], [0, -1.0]])
h = [80.0, 40.0, 64.0, 0.0, 0.0]
# 内積が目的関数
obj = cp.Maximize(c.T @ x)

# 制約Gx <= hを定義
cons = [G @ x <= h]
P = cp.Problem(obj, cons)
P.solve(verbose=True)
print(x.value)
