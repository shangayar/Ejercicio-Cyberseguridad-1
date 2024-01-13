import hashlib
import os

# Recorremos los archivos del directorio
def files(carpeta):
    lista = os.listdir(carpeta)
    return lista

def hashing(listfiles):
    m = hashlib.md5()
    with open(listfiles,"rb") as f:
        for chunk in iter(lambda: f.read(), b""):
            m.update(chunk)
    return (m.hexdigest())

def compare(hash):
    hashes = {"copia.sh": "90965b0eb20e68b7d0b59accd2a3b4fd", "log.txt": "0b29406e348cd5f17c2fd7b47b1012f9",
              "pass.txt": "6d5e43a730490d75968279b6adbd79ec", "plan-A.txt": "129ea0c67567301df1e1088c9069b946",
              "plan-B.txt": "4e9878b1c28daf4305f17af5537f062a", "script.py": "66bb9ec43660194bc066bd8b4d35b151"}

    for clave1 in hash:
        for clave2 in hashes:
            if clave1 == clave2:
                if hash[clave1] == hashes[clave2]:
                    print(f"El archivo {clave2} tiene integridad")
                else:
                    print(f"El archivo {clave2} NO tiene integridad")

##############################################
carpeta = "/home/cristian/Documentos/04_Cursos/30_Discord/cybersecurity/Ejercicio-Cyberseguridad-1/PyJ Systems/"

listfiles = files(carpeta)
checkhashing = {}

for file in listfiles:
    address = carpeta + file
    checkhashing.update({file:hashing(address)})
print(checkhashing)
compare(checkhashing)

