import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Juego de Preguntados")
root.geometry("1024x768") 

fondo = ImageTk.PhotoImage(Image.open("C:\\Users\\camiy\\Desktop\\Task\\proyecto Python\\img\\fondo.png"))
imagen_original = Image.open("C:\\Users\\camiy\\Desktop\\Task\\proyecto Python\\img\\imgMedio.png") 
ancho, alto = imagen_original.size
imagen_centrada = ImageTk.PhotoImage(imagen_original.resize((int(ancho * 1.5), int(alto * 1.5))))  

img_verdadero = ImageTk.PhotoImage(Image.open("C:\\Users\\camiy\\Desktop\\Task\\proyecto Python\\img\\verdadero.png"))
img_falso = ImageTk.PhotoImage(Image.open("C:\\Users\\camiy\\Desktop\\Task\\proyecto Python\\img\\falso.png"))

canvas = tk.Canvas(root, width=1024, height=768)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=fondo, anchor="nw")

canvas.create_image(512, 200, image=imagen_centrada, anchor="center") 

respuesta_img = canvas.create_image(20, 20, image=None, anchor="nw")  

preguntas = [
    {"pregunta": "¿Cuál es el deporte más popular del mundo?", "opciones": ["Baloncesto", "Fútbol", "Tenis", "Cricket"], "correcta": 1},
    {"pregunta": "¿Qué atleta ha ganado más medallas olímpicas en la historia?", "opciones": ["Usain Bolt", "Michael Phelps", "Carl Lewis", "Larisa Latynina"], "correcta": 1},
    {"pregunta": "¿En qué deporte se usa una canasta para anotar puntos?", "opciones": ["Fútbol", "Baloncesto", "Voleibol", "Rugby"], "correcta": 1},
    {"pregunta": "¿Cuál es la liga de fútbol más competitiva en Europa?", "opciones": ["La Liga \n (España)", "Serie A \n (Italia)", "Bundesliga \n (Alemania)", "Premier League \n (Inglaterra)"], "correcta": 3},
    {"pregunta": "¿Qué deporte combina natación, ciclismo y carrera a pie?", "opciones": ["Triatlón", "Duatlón", "Acuatlón", "Pentatlón"], "correcta": 0},
    {"pregunta": "¿En qué país se originó el béisbol?", "opciones": ["Japón", "Estados Unidos", "Cuba", "República \n Dominicana"], "correcta": 1},
    {"pregunta": "¿Qué deporte de combate se originó en Japón y se enfoca en el lanzamiento y control del oponente?", "opciones": ["Judo", "Karate", "Taekwondo", "Aikido"], "correcta": 0},
    {"pregunta": "¿Qué deporte se practica en un campo con banderas y hoyos?", "opciones": ["Golf", "Cricket", "Rugby", "Fútbol"], "correcta": 0},
    {"pregunta": "¿Quién es conocido como el 'Rey del Fútbol'?", "opciones": ["Diego Maradona", "Pelé", "Lionel Messi", "Cristiano Ronaldo"], "correcta": 1},
    {"pregunta": "¿Qué deporte se juega en un campo rectangular y se utiliza una pelota ovalada?", "opciones": ["Fútbol", "Rugby", "Balonmano", "Cricket"], "correcta": 1}
]

indice_pregunta = 0
puntuacion = 0

def mostrar_pregunta():
    global indice_pregunta

    if indice_pregunta >= len(preguntas):
        mostrar_resultados()
        return
    
    pregunta_actual = preguntas[indice_pregunta]
    pregunta_text.config(text=pregunta_actual["pregunta"])
    
    boton_rojo.config(text=pregunta_actual["opciones"][0], command=lambda: responder(0))
    boton_azul.config(text=pregunta_actual["opciones"][1], command=lambda: responder(1))
    boton_amarillo.config(text=pregunta_actual["opciones"][2], command=lambda: responder(2))
    boton_verde.config(text=pregunta_actual["opciones"][3], command=lambda: responder(3))

    canvas.itemconfig(respuesta_img, image='')  

def responder(opcion):
    global indice_pregunta, puntuacion
    
    correcta = preguntas[indice_pregunta]["correcta"]

    if opcion == correcta:
        puntuacion += 1
        canvas.itemconfig(respuesta_img, image=img_verdadero)  
    else:
        canvas.itemconfig(respuesta_img, image=img_falso)  
    root.after(1000, lambda: siguiente_pregunta())  

def siguiente_pregunta():
    global indice_pregunta
    indice_pregunta += 1
    mostrar_pregunta()

def mostrar_resultados():
    global puntuacion, indice_pregunta
    
    porcentaje = (puntuacion / len(preguntas)) * 100
    
    messagebox.showinfo("Resultados", f"Tu puntuación es: {puntuacion}/{len(preguntas)}\nPorcentaje de aciertos: {porcentaje:.2f}%")
    
    if puntuacion <= 3:
        retry = messagebox.askyesno("Mala Puntuación", "Sacaste 3 o menos puntos. ¿Quieres intentarlo de nuevo?")
        if retry:
            indice_pregunta = 0
            puntuacion = 0
            mostrar_pregunta()  
        else:
            root.destroy()  
    else:
        root.destroy() 


pregunta_text = tk.Label(root, text="", font=("Open sans", 23), wraplength=800, bg="#ffffff")
pregunta_text.place(relx=0.5, y=350, anchor="center") 

frame_botones = tk.Frame(root, bg="#ffffff")
frame_botones.place(relx=0.5, y=550, anchor="center")  

# Funciones para el botón rojo
def on_enter_rojo(event):
    boton_rojo.config(bg="#C52828")  

def on_leave_rojo(event):
    boton_rojo.config(bg="#FF3131")  # Color original

boton_rojo = tk.Button(frame_botones, text="", font=("Open sans", 22), width=15, height=2, bg="#FF3131", bd=5, relief="raised")
boton_rojo.grid(row=0, column=0, padx=20, pady=20)
boton_rojo.bind("<Enter>", on_enter_rojo)
boton_rojo.bind("<Leave>", on_leave_rojo)

# Funciones para el botón azul
def on_enter_azul(event):
    boton_azul.config(bg="#4861D2") 

def on_leave_azul(event):
    boton_azul.config(bg="#5271FF")  # Color original

boton_azul = tk.Button(frame_botones, text="", font=("Open sans", 22), width=15, height=2, bg="#5271FF", bd=5, relief="raised")
boton_azul.grid(row=0, column=1, padx=20, pady=20)
boton_azul.bind("<Enter>", on_enter_azul)
boton_azul.bind("<Leave>", on_leave_azul)

# Funciones para el botón amarillo
def on_enter_amarillo(event):
    boton_amarillo.config(bg="#E0C453")  # Cambia a un tono más oscuro

def on_leave_amarillo(event):
    boton_amarillo.config(bg="#FFDE59")  # Color original

boton_amarillo = tk.Button(frame_botones, text="", font=("Open sans", 22), width=15, height=2, bg="#FFDE59", bd=5, relief="raised")
boton_amarillo.grid(row=1, column=0, padx=20, pady=20)
boton_amarillo.bind("<Enter>", on_enter_amarillo)
boton_amarillo.bind("<Leave>", on_leave_amarillo)

# Funciones para el botón verde
def on_enter_verde(event):
    boton_verde.config(bg="#6DB94C")  

def on_leave_verde(event):
    boton_verde.config(bg="#7ED952")  # Color original

boton_verde = tk.Button(frame_botones, text="", font=("Open sans", 22), width=15, height=2, bg="#7ED952", bd=5, relief="raised")
boton_verde.grid(row=1, column=1, padx=20, pady=20)
boton_verde.bind("<Enter>", on_enter_verde)
boton_verde.bind("<Leave>", on_leave_verde)

mostrar_pregunta()

root.mainloop()
