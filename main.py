import socket as s

if __name__ == '__main__':
    print("Inicializando el servidor en la dirección 127.10.10.10, puerto 3000")
    server = s.socket(s.AF_INET, s.SOCK_STREAM)
    server.bind(("127.10.10.10", 3000))
    server.listen()
    conexion,info = server.accept()
    print(f'Se ha establecido una conexión en la direccion: {info}')
    while conexion:
        datos = conexion.recv(2000)
        if(datos):
            print(f'Como servidor hemos recibido: {datos}')
        else:
            break
