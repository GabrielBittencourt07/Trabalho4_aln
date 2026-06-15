import numpy as np
import matplotlib.pyplot as plt

# Criando o vetor ômega variando de 0 a 1
omega = np.linspace(0, 1, 100)

# 1. Autovalores (vamos plotar apenas a parte imaginária)
lambda1_imag = omega
lambda2_imag = -omega

# 2. Autovetores (vamos plotar a parte imaginária da 2ª coordenada)
v1_coord2_imag = omega
v2_coord2_imag = -omega

# Criando a figura com 2 gráficos lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Gráfico 1: Autovalores ---
ax1.plot(omega, lambda1_imag, label='Im(λ1) = ω', color='blue')
ax1.plot(omega, lambda2_imag, label='Im(λ2) = -ω', color='red', linestyle='--')
ax1.set_title('Autovalores de A(ω)')
ax1.set_xlabel('ω')
ax1.set_ylabel('Parte Imaginária')
ax1.grid(True, linestyle=':')
ax1.legend()

# --- Gráfico 2: Autovetores ---
ax2.plot(omega, v1_coord2_imag, label='Im(v1_y) = ω', color='blue')
ax2.plot(omega, v2_coord2_imag, label='Im(v2_y) = -ω', color='red', linestyle='--')
ax2.set_title('2ª Coordenada dos Autovetores')
ax2.set_xlabel('ω')
ax2.set_ylabel('Parte Imaginária')
ax2.grid(True, linestyle=':')
ax2.legend()

plt.tight_layout()
plt.show()
