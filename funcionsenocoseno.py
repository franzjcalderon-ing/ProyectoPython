import tkinter as tk
from tkinter import ttk, filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar_funciones():
    try:
        A = float(entry_A.get())
        B = float(entry_B.get())
        C = float(entry_C.get())
        D = float(entry_D.get())
    except ValueError:
        resultado.set("Error: Ingresa valores numéricos válidos.")
        return

    seleccionadas = []
    if var_seno.get():
        seleccionadas.append("Seno")
    if var_coseno.get():
        seleccionadas.append("Coseno")

    if not seleccionadas:
        resultado.set("Error: Selecciona al menos una función.")
        return

    x = np.linspace(-2*np.pi, 2*np.pi, 1000)
    ax.clear()

    colores = {
        "Seno": "#1f77b4",
        "Coseno": "#2ca02c",
    }

    for funcion in seleccionadas:
        if funcion == "Seno":
            y = A * np.sin(B * x + C) + D
            ax.plot(x, y, label=f"{A}·sen({B}x + {C}) + {D}", color=colores[funcion], linewidth=2)
        elif funcion == "Coseno":
            y = A * np.cos(B * x + C) + D
            ax.plot(x, y, label=f"{A}·cos({B}x + {C}) + {D}", color=colores[funcion], linewidth=2)

    ax.set_facecolor("#f0f0f0")
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_ylim(-A-2, A+2)

    ax.set_xticks(np.linspace(-2*np.pi, 2*np.pi, 9))
    ax.set_yticks(np.arange(int(-A-2), int(A+3), 1))
    ax.tick_params(axis='both', which='major', labelsize=10)

    secax = ax.secondary_xaxis('top')
    secax.set_xticks([-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    secax.set_xticklabels([r"$-2\pi$", r"$-\frac{3\pi}{2}$", r"$-\pi$", r"$-\frac{\pi}{2}$",
                           r"$0$", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])
    secax.tick_params(axis='x', labelsize=10)

    ax.set_title("Gráficas de Seno y Coseno", fontsize=16)
    ax.set_xlabel("Eje X (decimales)", fontsize=14)
    secax.set_xlabel("Eje X (radianes)", fontsize=14)
    ax.set_ylabel("Eje Y", fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(loc="upper right", framealpha=0.9)
    canvas.draw()

def guardar_imagen():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                             filetypes=[("Archivo PNG", "*.png")])
    if file_path:
        fig.savefig(file_path)
        resultado.set(f"Imagen guardada en: {file_path}")

def limpiar():
    entry_A.delete(0, tk.END)
    entry_A.insert(0, "1.0")
    entry_B.delete(0, tk.END)
    entry_B.insert(0, "1.0")
    entry_C.delete(0, tk.END)
    entry_C.insert(0, "0.0")
    entry_D.delete(0, tk.END)
    entry_D.insert(0, "0.0")
    var_seno.set(True)
    var_coseno.set(False)
    resultado.set("")
    ax.clear()
    canvas.draw()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Graficador de Seno y Coseno con Radianes")
root.geometry("1000x750")

# Frame principal para controles
frame_controles = ttk.Frame(root, padding="10")
frame_controles.pack(fill=tk.X)

# Sub-frame centrado para entradas
frame_centrado = ttk.Frame(frame_controles)
frame_centrado.pack(anchor="center")

# Checkbox para seleccionar funciones
var_seno = tk.BooleanVar(value=True)
var_coseno = tk.BooleanVar()

ttk.Label(frame_centrado, text="Funciones:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
ttk.Checkbutton(frame_centrado, text="Seno", variable=var_seno).grid(row=0, column=1, padx=5, pady=5)
ttk.Checkbutton(frame_centrado, text="Coseno", variable=var_coseno).grid(row=0, column=2, padx=5, pady=5)

# Entradas de parámetros
ttk.Label(frame_centrado, text="A (Amplitud):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_A = ttk.Entry(frame_centrado)
entry_A.grid(row=1, column=1, padx=5, pady=5)
entry_A.insert(0, "1.0")

ttk.Label(frame_centrado, text="B (Frecuencia):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
entry_B = ttk.Entry(frame_centrado)
entry_B.grid(row=2, column=1, padx=5, pady=5)
entry_B.insert(0, "1.0")

ttk.Label(frame_centrado, text="C (Fase):").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
entry_C = ttk.Entry(frame_centrado)
entry_C.grid(row=3, column=1, padx=5, pady=5)
entry_C.insert(0, "0.0")

ttk.Label(frame_centrado, text="D (Desplazamiento):").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
entry_D = ttk.Entry(frame_centrado)
entry_D.grid(row=4, column=1, padx=5, pady=5)
entry_D.insert(0, "0.0")

# Botones
boton_graficar = ttk.Button(frame_centrado, text="Graficar", command=graficar_funciones)
boton_graficar.grid(row=5, column=0, pady=10)

boton_guardar = ttk.Button(frame_centrado, text="Guardar Imagen", command=guardar_imagen)
boton_guardar.grid(row=5, column=1, pady=10)

boton_limpiar = ttk.Button(frame_centrado, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=5, column=2, pady=10)

# Resultado
resultado = tk.StringVar()
ttk.Label(frame_centrado, textvariable=resultado).grid(row=6, column=0, columnspan=3, pady=5)

# Frame para gráfico
frame_grafico = ttk.Frame(root)
frame_grafico.pack(fill=tk.BOTH, expand=True)

# Canvas de Matplotlib
fig, ax = plt.subplots(figsize=(12, 6))
canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Iniciar la ventana
root.mainloop()