import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título
st.title("Graficador de función Sen y Cos")

# Sidebar con entradas de parámetros
st.sidebar.header("Parámetros de la función")
A = st.sidebar.number_input("A (Amplitud)", value=1.0)
B = st.sidebar.number_input("B (Frecuencia)", value=1.0)
C = st.sidebar.number_input("C (Fase)", value=0.0)
D = st.sidebar.number_input("D (Desplazamiento)", value=0.0)

# Selección de funciones
st.sidebar.header("Funciones a graficar")
graficar_seno = st.sidebar.checkbox("Seno", value=True)
graficar_coseno = st.sidebar.checkbox("Coseno", value=False)

# Validación
if not graficar_seno and not graficar_coseno:
    st.error("Selecciona al menos una función para graficar.")
else:
    # Generar valores de x
    x = np.linspace(-2*np.pi, 2*np.pi, 1000)
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(10, 5))

    if graficar_seno:
        y_seno = A * np.sin(B * x + C) + D
        ax.plot(x, y_seno, label=f"{A}·sen({B}x + {C}) + {D}", color="#1f77b4")

    if graficar_coseno:
        y_coseno = A * np.cos(B * x + C) + D
        ax.plot(x, y_coseno, label=f"{A}·cos({B}x + {C}) + {D}", color="#2ca02c")

    ax.set_xticks(np.linspace(-2*np.pi, 2*np.pi, 9))
    ax.set_xticklabels([r"$-2\pi$", r"$-\frac{3\pi}{2}$", r"$-\pi$", r"$-\frac{\pi}{2}$", r"$0$", 
                        r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])
    ax.set_xlabel("Eje X (radianes)")
    ax.set_ylabel("Eje Y")
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_ylim(-A-2, A+2)
    ax.grid(True, linestyle="--", alpha=0.7)
    ax.legend()

    st.pyplot(fig)
