import datetime
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
#https://medium.com/@abdelhedihlel/upload-files-to-firebase-storage-using-python-782213060064
db_c = firestore.client()
#DEBEMOS DE INGRESAR EL NOMBRE DEL ARCHIVO AQUI
fileName = "mujer.png"
#nombre_buscar = input("ingresa el nombre del archivo: ")
bucket = storage.bucket()
nombres_img = []
#FORMA PARA SUBIR ARCHIVO
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)
blob.make_public()
print("Info de la foto ", blob.id, blob.public_url)
    #storage_client = storeCloud.Client()
    #blobs = storage_client.list_blobs("")
    #for blob in blobs:
    #    print(blob)
for blob in bucket.list_blobs():
    print(blob)
    nombres_img.append(blob.name)
    blob.make_public()
    print(blob.public_url)#presenta un enlace sin necesidad de descargar la imagen
    #name = str(blob.name)
    #print(name)
    #blob_img = bucket.blob(name)
    #funciona para descargar las imagenes guardadas
    #blob_img.download_to_filename(name)
        #X_url = blob_img.generate_signed_url(datetime.timedelta(seconds=3000), method='GET')
        #print(X_url)

#for i in nombres_img:
#    if(nombre_buscar == i):
#        print(i)