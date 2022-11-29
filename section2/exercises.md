# 第 2 章 練習問題 答案

## 2.1

> 1.1 節の例 1.2 の輸送問題を、線形計画問題として定式化せよ。

倉庫$S_i$から顧客$C_j$に輸送する量を$x_{ij}$とする

倉庫に保管してある量についての制約は

$$
\sum_{j=1}^3 x_{ij} \leqq \left\{ \begin{aligned}
  20(i = 1)\\
  15(i = 2)
\end{aligned} \right.
$$

と書け、各工場の需要に対する制約は

$$
\sum_{i=1}^2 x_{ij} \geqq \left\{\begin{aligned}
  8.5(j = 1)\\
  12.5(j = 2)\\
  14(j = 3)
\end{aligned}\right.
$$

と書ける。

したがって、線形計画問題として定式化すると

$$
\begin{aligned}
\textrm{Minimize}  ~~~~&  x_{11} + 2x_{12} + 3x_{13} + 4x_{21} + 8x_{22} + 7x_{23}\\
\textrm{subject ~ to}  ~~~~&  x_{11} + x_{12} + x_{13} \leqq 20\\
&  x_{21} + x{22} + x_{23} \leqq 15\\
&  x_{11} + x_{21} \geqq 8.5\\
&  x_{12} + x_{22} \geqq 12.5\\
&  x_{13} + x_{23} \geqq 14
\end{aligned}
$$

となる。これを等式標準形で表したい。

**TODO: 等式標準形で書く**

$$
\begin{aligned}
\boldsymbol X &=
\begin{pmatrix}
x_{11} & x_{12} & x_{13}\\
x_{21} & x_{22} & x_{23}
\end{pmatrix}\\
A &=
\end{aligned}
$$
