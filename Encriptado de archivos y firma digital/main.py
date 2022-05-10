import socket as s
import nacl.secret
import nacl.utils
import nacl.pwhash
from nacl.signing import VerifyKey
from nacl.pwhash.argon2i import kdf

if __name__ == '__main__':
    print("Inicializando el servidor en la dirección 127.10.10.10, puerto 3000")
    server = s.socket(s.AF_INET, s.SOCK_STREAM)
    server.bind(("127.10.10.10", 3000))
    server.listen()
    conexion,info = server.accept()

    datos = conexion.recv(4096).decode()
    print(datos)
    name, size = datos.split(' ')

    size = int(size)
    print(f'Se ha recibido: {name} con un peso de {size} Bytes')
    save = open(r"C:\Users\CAQUIRAR_MX\PycharmProjects\Random_number_SERVER\archivo_a_escribir.txt", "wb")

    print(f'Se ha establecido una conexión en la direccion: {info}')
    cliente_keybytes = conexion.recv(32)
    cliente_signature = conexion.recv(64)
    datos_nuevos = b''
    datos_completos = b''
    while True:
        datos_nuevos = conexion.recv(4096)
        datos_completos += datos_nuevos
        if(datos_nuevos):
            print(f'Se ha recibido: {datos_nuevos}')
        else:
            break
    conexion.close()
    # Create a VerifyKey object from a hex serialized public key
    verify_key = VerifyKey(cliente_keybytes)

    # Check the validity of a message's signature
    # The message and the signature can either be passed together, or
    # separately if the signature is decoded to raw bytes.
    # These are equivalent:
    print('Se ha podido verificar con la clave que el archivo después de la llave es:')
    print(verify_key.verify(datos_completos, cliente_signature))

    nacl.secret.SecretBox.KEY_SIZE
    kdf = nacl.pwhash.argon2i.kdf
    salt_size = nacl.pwhash.argon2i.SALTBYTES
    salt = nacl.utils.random(salt_size)
    key = kdf(nacl.secret.SecretBox.KEY_SIZE, 'practica'.encode("utf-8"), salt)
    box = nacl.secret.SecretBox(key)
    encrypted = box.encrypt(datos_completos)
    save.write(encrypted)