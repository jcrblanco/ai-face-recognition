import cv2
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk

# Directorio donde se guardarán las caras
caras_dir = "caras"

# Función para capturar y guardar la imagen
def capture_image(name):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Error", "No se pudo acceder a la cámara")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "No se pudo leer el fotograma de la cámara")
            break

        # Mostrar el recuadro en la cara detectada
        cv2.putText(frame, "Alinea tu cara en el recuadro y presiona 'c' para capturar", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Definir un área de recuadro en el centro de la pantalla
        height, width, _ = frame.shape
        top_left = (int(width/2 - 100), int(height/2 - 100))
        bottom_right = (int(width/2 + 100), int(height/2 + 100))

        # Dibujar el recuadro en la imagen
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

        # Mostrar el fotograma
        cv2.imshow('Captura de imagen', frame)

        # Esperar a que el usuario presione 'c' para capturar la imagen
        if cv2.waitKey(1) & 0xFF == ord('c'):
            # Recortar la imagen al área del recuadro
            cropped_frame = frame[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

            # Guardar la imagen con el nombre proporcionado
            file_path = os.path.join(caras_dir, f"{name}.jpg")
            cv2.imwrite(file_path, cropped_frame)
            messagebox.showinfo("Éxito", f"Imagen guardada como {name}.jpg")
            break

    cap.release()
    cv2.destroyAllWindows()

# Función para iniciar el proceso de onboarding
def start_onboarding():
    name = simpledialog.askstring("Nombre", "Escribe tu nombre:")
    if name:
        capture_image(name)

# Función para cerrar la aplicación
def close_app():
    root.destroy()

# Crear la interfaz de usuario
root = tk.Tk()
root.title("Onboarding de Caras")

# Configurar el tamaño de la ventana
root.geometry("400x200")

# Etiqueta de bienvenida
welcome_label = tk.Label(root, text="Bienvenido al Onboarding de Caras", font=("Arial", 14))
welcome_label.pack(pady=20)

# Botón para iniciar el onboarding
start_button = tk.Button(root, text="Iniciar Onboarding", command=start_onboarding, font=("Arial", 12))
start_button.pack(pady=10)

# Botón para cerrar la aplicación
close_button = tk.Button(root, text="Cerrar", command=close_app, font=("Arial", 12))
close_button.pack(pady=10)

# Crear el directorio de caras si no existe
if not os.path.exists(caras_dir):
    os.makedirs(caras_dir)

# Iniciar el bucle principal de la aplicación
root.mainloop()
