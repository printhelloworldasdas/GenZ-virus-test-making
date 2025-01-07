import tkinter as tk  
import random  
import time  
import threading  
import pyautogui  # Asegúrate de que tienes esta biblioteca instalada  

# Crear la ventana principal  
root = tk.Tk()  
root.title("Infected by GenZ.exe")  
root.geometry("0x0")  # Ventana principal invisible  
root.overrideredirect(True)  # Sin bordes  

# Variable para controlar si el mouse se está moviendo  
mouse_moving = False  

# Función para crear el texto flotante  
def create_floating_text():  
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

    # Mantener la ventana flotante visible durante 35 segundos  
    float_window.after(35000, float_window.destroy)  # Desaparece después de 35 segundos  

    # Hacer la ventana no cerrable  
    float_window.protocol("WM_DELETE_WINDOW", lambda: None)  

# Función para mover el mouse a posiciones aleatorias  
def move_mouse():  
    global mouse_moving  
    mouse_moving = True  
    while mouse_moving:  
        screen_width, screen_height = pyautogui.size()  
        x = random.randint(0, screen_width - 1)  
        y = random.randint(0, screen_height - 1)  
        pyautogui.moveTo(x, y, duration=0.5)  
        time.sleep(1)  

# Efecto de pantalla invertida  
def upside_down_effect():  
    global mouse_moving  
    # Esperar un momento antes de comenzar (simulando el efecto durante 20 segundos)  
    root.attributes("-fullscreen", True)  # Pantalla completa  
    time.sleep(20)  # Mantener la pantalla en modo completo por 20 segundos  
    root.attributes("-fullscreen", False)  # Vuelve a la normalidad  
    
    # Detener el movimiento del mouse después del efecto de "upside-down"  
    mouse_moving = False  
    # Iniciar efecto de derretimiento después de "upside-down"  
    melting_effect()  

# Función que simula el efecto "derretido"  
def melting_effect():  
    canvas = tk.Canvas(root, width=800, height=600, bg="black")  
    canvas.pack()  

    # Crea un rectángulo que se "derretirá"  
    rect = canvas.create_rectangle(0, 0, 800, 600, fill="red")  

    for i in range(150):  # Animación por 150 frames para 15 segundos  
        canvas.move(rect, 0, 1)  # Mover el rectángulo hacia abajo lentamente  
        canvas.config(bg="black")  # Fondo negro  
        root.update()  # Actualizar ventana  
        time.sleep(0.1)  # Controlar la velocidad de la animación  

        # Alternar opacidad  
        if i % 10 < 5:  
            canvas.itemconfig(rect, fill="red", outline="")  
        else:  
            canvas.itemconfig(rect, fill="black", outline="")  

    # Eliminar el canvas de la ventana  
    canvas.destroy()  

# Iniciar las funciones al principio  
create_floating_text()  
move_mouse_thread = threading.Thread(target=move_mouse)  
move_mouse_thread.start()  
upside_down_thread = threading.Thread(target=upside_down_effect)  
upside_down_thread.start()  

# Mantener la ventana principal abierta  
root.mainloop()
