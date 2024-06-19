#porownanie trajektorii dla roznych r
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

sigma = 10
beta = 8/3

def uklad_rownan(vector, t, sigma, beta, r):
    x, y, z = vector
    d_vector = [
        sigma*(y - x),
        x*(r - z) - y,
        x*y - beta*z
    ]
    return d_vector

pozycja_0_1 = [0.0, 1.0, 1.0]
punkty_czasowe = np.linspace(0, 40, 10001)

# Rozwiązania dla r = 24.74
r1 = 24.74
pozycje_1_r1 = odeint(uklad_rownan, pozycja_0_1, punkty_czasowe, args=(sigma, beta, r1))
x_sol_1_r1, y_sol_1_r1, z_sol_1_r1 = pozycje_1_r1[:, 0], pozycje_1_r1[:, 1], pozycje_1_r1[:, 2]

# Rozwiązania dla r = 28
r2 = 28
pozycje_1_r2 = odeint(uklad_rownan, pozycja_0_1, punkty_czasowe, args=(sigma, beta, r2))
x_sol_1_r2, y_sol_1_r2, z_sol_1_r2 = pozycje_1_r2[:, 0], pozycje_1_r2[:, 1], pozycje_1_r2[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Wykres dla r = 24.74
ax.plot(x_sol_1_r1, y_sol_1_r1, z_sol_1_r1, 'red', label=f'r = {r1}')

# Wykres dla r = 28
ax.plot(x_sol_1_r2, y_sol_1_r2, z_sol_1_r2, 'blue', label=f'r = {r2}')

ax.set_title('Porównanie trajektorii dla różnych wartości r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()