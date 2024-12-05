# Importa o Streamlit
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título da página
st.title("Exemplo de Aplicação com Streamlit")

# Criando um slider para ajustar o número de pontos
num_points = st.slider("Escolha o número de pontos", min_value=10, max_value=100, value=50)

# Gerando dados aleatórios
x = np.linspace(0, 10, num_points)
y = np.sin(x) + np.random.normal(0, 0.1, num_points)

# Exibindo um gráfico
st.write(f"Gerando {num_points} pontos de dados com ruído")
fig, ax = plt.subplots()
ax.plot(x, y, label="Dados com ruído")
ax.set_title("Gráfico de Dados Aleatórios com Ruído")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
st.pyplot(fig)
