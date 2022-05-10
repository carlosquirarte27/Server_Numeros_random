import nacl.utils
import socket as s
import os
from nacl.signing import SigningKey


if __name__ == '__main__':
  print("Nuevo cliente, preparado para conectarse a la 127.10.10.10 en el puerto 3000")
  size = os.path.getsize(r"C:\Users\CAQUIRAR_MX\PycharmProjects\Random_number_SERVER\archivo_a_enviar.txt")
  filename = r"C:\Users\CAQUIRAR_MX\PycharmProjects\Random_number_SERVER\archivo_a_enviar.txt"
  cliente = s.socket(s.AF_INET, s.SOCK_STREAM)
  cliente.connect(("127.10.10.10", 3000))
  cliente.send(f'{filename} {size}'.encode())
  with open(r'C:\Users\CAQUIRAR_MX\PycharmProjects\Random_number_SERVER\archivo_a_enviar.txt', "rb") as file:
    read = file.read()
    # Generate a new random signing key
    signing_key = SigningKey.generate()

    # Sign a message with the signing key
    signed = signing_key.sign(read)

    # Obtain the verify key for a given signing key
    verify_key = signing_key.verify_key

    # Serialize the verify key to send it to a third party
    verify_key_bytes = verify_key.encode()
    cliente.sendall(verify_key_bytes)
    cliente.sendall(signed.signature)
    cliente.sendall(read)