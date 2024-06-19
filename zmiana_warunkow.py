#porównanie trajektorii dla róznych warunków początkowych
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parametry Lorenza
sigma = 10
beta = 8/3
r = 24.74  # Zmienna r, zmień jej wartość, aby zobaczyć różne zachowania układu

# Funkcja definiująca układ równań Lorenza
def uklad_rownan(vector, t, sigma, beta, r):
    x, y, z = vector
    d_vector = [
        sigma*(y - x),
        x*(r - z) - y,
        x*y - beta*z
    ]
    return d_vector

# Warunki początkowe wartośc w t=0
pozycja_0_1 = [0.0, 1.0, 1.0]  # Pierwszy zestaw warunków początkowych
pozycja_0_2 = [1.0, 2.1, 3.0]  # Drugi zestaw warunków początkowych

# Punkty czasowe
punkty_czasowe = np.linspace(0, 40, 10001)

# Rozwiązania dla pierwszego zestawu warunków początkowych
pozycje_1 = odeint(uklad_rownan, pozycja_0_1, punkty_czasowe, args=(sigma, beta, r))
x_sol_1, y_sol_1, z_sol_1 = pozycje_1[:, 0], pozycje_1[:, 1], pozycje_1[:, 2]

# Rozwiązania dla drugiego zestawu warunków początkowych
pozycje_2 = odeint(uklad_rownan, pozycja_0_2, punkty_czasowe, args=(sigma, beta, r))
x_sol_2, y_sol_2, z_sol_2 = pozycje_2[:, 0], pozycje_2[:, 1], pozycje_2[:, 2]

# Tworzenie wykresu
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Wykres dla pierwszego zestawu warunków początkowych
ax.plot(x_sol_1, y_sol_1, z_sol_1, 'red', label=f'Pozycja początkowa 1: {pozycja_0_1}')

# Wykres dla drugiego zestawu warunków początkowych
ax.plot(x_sol_2, y_sol_2, z_sol_2, 'blue', label=f'Pozycja początkowa 2: {pozycja_0_2}')

# Ustawienia wykresu
ax.set_title('Porównanie trajektorii dla różnych warunków początkowych')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Wyświetlenie wykresu
plt.show()
