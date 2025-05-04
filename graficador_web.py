
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Graficador de Seno y Coseno")

st.title("🧮 Graficador de Seno y Coseno con Radianes")

st.sidebar.header("Parámetros de la función")
A = st.sidebar.number_input("A (Amplitud)", value=1.0)
B = st.sidebar.number_input("B (Frecuencia)", value=1.0)
C = st.sidebar.number_input("C (Fase)", value=0.0)
D = st.sidebar.number_input("D (Desplazamiento)", value=0.0)

st.sidebar.header("Funciones a graficar")
graficar_seno = st.sidebar.checkbox("Seno", value=True)
graficar_coseno = st.sidebar.checkbox("Coseno", value=False)

if not graficar_seno and not graficar_coseno:
    st.error("Selecciona al menos una función para graficar.")
    st.stop()

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
fig, ax = plt.subplots(figsize=(12, 6))

colores = {
    "Seno": "#1f77b4",
    "Coseno": "#2ca02c",
}

if graficar_seno:
    y = A * np.sin(B * x + C) + D
    ax.plot(x, y, label=f"{A}·sen({B}x + {C}) + {D}", color=colores["Seno"], linewidth=2)
if graficar_coseno:
    y = A * np.cos(B * x + C) + D
    ax.plot(x, y, label=f"{A}·cos({B}x + {C}) + {D}", color=colores["Coseno"], linewidth=2)

ax.set_facecolor("#f0f0f0")
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_ylim(-A-2, A+2)
ax.set_xticks(np.linspace(-2*np.pi, 2*np.pi, 9))
ax.set_yticks(np.arange(int(-A-2), int(A+3), 1))
ax.tick_params(axis='both', which='major', labelsize=10)
ax.set_title("Gráficas de Seno y Coseno", fontsize=16)
ax.set_xlabel("Eje X (radianes)", fontsize=14)
ax.set_ylabel("Eje Y", fontsize=14)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc="upper right", framealpha=0.9)
st.pyplot(fig)
