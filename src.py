import numpy as np
from scipy import linalg
# 定数を定義
m = 1      # 必要に応じて設定
M = 1      # 必要に応じて設定
g = 9.81   # 重力加速度
l = 1      # ペンデュラムの長さ

# 行列 A, B, Q の定義
A = np.array([[0, 0, 1, 0],
              [0, 0, 0, 1],
              [0, -3 * m * g / (m + 4 * M), 0, 0],
              [0, 3 * (M + m) * g / (l * (m + 4 * M)), 0, 0]])

B = np.array([[0],
              [0],
              [4 / (m + 4 * M)],
              [-3 / ((m + 4 * M) * l)]])

Q = np.diag([100, 100, 1, 1])

# リカッチ方程式の解を求める
R = linalg.solve_continuous_are(A, B, Q, np.eye(1))  # R を求める

# B^T * R を計算
BT_R = B.T @ R
print("Matrix B^T * R:")
print(BT_R)
