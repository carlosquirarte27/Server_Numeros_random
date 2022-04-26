import nacl.utils
import socket as s
import os

if __name__ == '__main__':
  print("Nuevo cliente, preparado para conectarse a la 127.10.10.10 en el puerto 3000")
  size = os.path.getsize(r'C:\Users\CAQUIRAR_MX\PycharmProjects\Random_number_SERVER\archivo_a_enviar.txt')
  filename = r"C:\Users\CAQUIRAR_MX\PycharmProjects\Random_number_SERVER/archivo_a_enviar.txt"
  cliente = s.socket(s.AF_INET, s.SOCK_STREAM)
  cliente.connect(("127.10.10.10", 3000))
  cliente.send(f'{filename} {size}'.encode())
  file = open(r'C:\Users\CAQUIRAR_MX\PycharmProjects\Random_number_SERVER\archivo_a_enviar.txt', "rb")
  read = file.read(4096)
  while(read):
    print(f"Se enviará {read}")
    cliente.sendall(read)
    read = file.read(4096)
