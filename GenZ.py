import tkinter as tk  
import random  
import math

# Crear la ventana principal  
root = tk.Tk()
root.title("Infected by GenZ.exe")
root.geometry("0x0")  # Ventana principal invisible  
root.overrideredirect(True)  # Sin bordes

# Función para crear el texto flotante  
def create_floating_text():
    if time_elapsed < 35000:  # Mostrar texto por 35 segundos  
        float_window = tk.Toplevel()
        float_window.overrideredirect(True)  # Sin bordes  
        float_window.wm_attributes("-topmost", True)  # Siempre encima  
        float_window.wm_attributes("-alpha", 0.7)  # Ventana semi-transparente

        # Crear la etiqueta con el texto "Infected by GenZ.exe"
        label = tk.Label(float_window, text="Infected by GenZ.exe", font=("Arial", 24), fg="red", bg="black")
        label.pack()

        # Posicionar la ventana en una ubicación aleatoria  
        screen_width = float_window.winfo_screenwidth()
        screen_height = float_window.winfo_screenheight()
        x = random.randint(0, screen_width - 300)
        y = random.randint(0, screen_height - 50)
        float_window.geometry(f"+{x}+{y}")

        # Mantener la ventana flotante visible  
        # Desaparece solo después del tiempo total  
        root.after(random.randint(300, 500), create_floating_text)  # Llama de nuevo aleatoriamente

# Función para crear el efecto de agujero negro  
def black_hole_effect():
    effect_window = tk.Toplevel()
    effect_window.geometry("800x600")  # Tamaño de la ventana del efecto  
    effect_window.wm_attributes("-topmost", True)  # Siempre encima  
    effect_window.wm_attributes("-alpha", 0.7)  # Ventana semi-transparente  
    effect_window.configure(bg="black")

    # Crear un canvas para dibujar el efecto  
    canvas = tk.Canvas(effect_window, width=800, height=600, bg="black")
    canvas.pack()

    # Animación del agujero negro  
    for i in range(100):
        radius = 10 + i * 5  # Aumentar el radio  
        x0 = 400 - radius  
        y0 = 300 - radius  
        x1 = 400 + radius  
        y1 = 300 + radius  
        canvas.create_oval(x0, y0, x1, y1, fill="black", outline="")
        effect_window.update()
        effect_window.after(50)

    # Efecto de pantalla invertida  
    for direction in range(20):  # Mover en 20 pasos  
        for dx, dy in [(-10, 0), (10, 0), (0, -10), (0, 10)]:  # Izquierda, derecha, arriba, abajo  
            effect_window.geometry(f"+{400 + dx * direction}+{300 + dy * direction}")
            effect_window.update()
            effect_window.after(50)

    effect_window.destroy()  # Cerrar la ventana después del efecto

# Tiempo de ejecución  
time_elapsed = 0

# Iniciar la creación del texto flotante  
create_floating_text()

# Hacer un bucle para contar el tiempo  
def count_time():
    global time_elapsed  
    time_elapsed += 300  # Incrementar cada 300 ms  
    if time_elapsed >= 35000:  # Si han pasado 35 segundos  
        black_hole_effect()  # Activar el efecto de agujero negro  
    else:
        root.after(300, count_time)  # Continuar contando

count_time()  # Iniciar el conteo del tiempo

# Mantener la ventana principal abierta  
root.mainloop()
