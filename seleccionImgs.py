from tkinter import *
from tkinter import filedialog
import firebase_admin
#import pyrebase
from firebase_admin import db, storage
from firebase_admin import firestore, credentials
from google.cloud import storage as storeCloud

config= {
    "apiKey": "AIzaSyBAn65WV8wmy80E_7mw2-OLH5sFQ8T0rTI",
    "authDomain": "store-collector.firebaseapp.com",
    "projectId": "store-collector",
    "storageBucket": "store-collector.appspot.com",
    "serviceAccount" : "service-account-key.json"
}
cred_obj = credentials.Certificate("./service-account-key.json")
firebase_admin.initialize_app(cred_obj, config)

#def getAllImages():

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/", title="Selecciona un archivo", filetypes=(("image files", "*.jpg"), ("image files", "*.png")))

    label_file_explorer.configure(text="Archivo abierto: "+filename)
    
    print(filename)
    nombreArchivo = filename.split('/')
    print(nombreArchivo[len(nombreArchivo)-1])
    subirImg(filename)

def subirImg(nombreArchivo):
    bucket = storage.bucket()
    nombre = nombreArchivo.split('/')
    nombreAr = nombre[len(nombre)-1]
    blob = bucket.blob(nombreAr)
    blob.upload_from_filename(nombreAr)
    #blob.upload_from_string(nombreArchivo, content_type="image/png")
    #blob.upload_from_filename(nombreArchivo)

window = Tk()

window.title('Buscador de archivos')

window.geometry("500x500")

window.config(background="white")

label_file_explorer = Label(window, text="Prueba de firestore", width=100, height=4, fg="black")

button_explore = Button(window, text="Selecciona un archivo", command=browseFiles)

button_subir = Button(window, text="Subir imagen", command=subirImg)

button_exit = Button(window, text="SALIR", command= exit)


label_file_explorer.grid(column=1, row=1)
button_explore.grid(column=1, row=2)
button_subir.grid(column=1, row=3)
button_exit.grid(column=1, row=4)

window.mainloop()