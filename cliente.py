import nacl.utils
import socket as s

if __name__ == '__main__':
  cliente = s.socket(s.AF_INET, s.SOCK_STREAM)
  cliente.connect(("127.10.10.10", 3000))
  print("Nuevo cliente, preparado para conectarse a la 127.10.10.10 en el puerto 3000")
  a = 64
  a = nacl.utils.random(a)
  print("Como cliente mandaremos al servidor :", a)
  cliente.sendall(a)
