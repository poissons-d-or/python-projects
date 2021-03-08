import numpy as np
import matplotlib.pyplot as plt

plt.figure()

LX, LY = 5, 5   # メッシュのためのパラメータ
gridwidth = 0.33
X, Y = np.meshgrid(np.arange(-LX, LX, gridwidth),
                   np.arange(-LY, LY, gridwidth))  # メッシュ生成

'''
R = np.sqrt(X**2+Y**2)  # 原点からの距離

# 点電荷の位置座標と電荷
X1, Y1 = 0, 0   # 原点への電荷の配置
Q1 = 1       # 電荷量の設定
R1 = np.sqrt((X-X1)**2+(Y-Y1)**2)  # この電荷から任意点(X,Y)までの距離
plt.plot(X1, Y1, 'o', color='blue')  # 点電荷を描画

# ベクトル関数 F(U(x,y), V(x,y))を定義。静電場の表式を用いる。
U = Q1*(X-X1)/(R1**2)
V = Q1*(Y-Y1)/(R1**2)
'''

U = X-Y
V = X+Y

plt.quiver(X, Y, U, V, color='red', angles='xy',
           scale_units='xy', scale=5.0)  # ベクトル場をプロット

plt.xlim([-LX, LX])  # 描くXの範囲
plt.ylim([-LY, LY])  # 描くyの範囲

# グラフ描画
plt.grid()
plt.draw()
plt.show()
