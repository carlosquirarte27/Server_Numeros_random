import socket as s

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
    while conexion:
        datos_nuevos = conexion.recv(4096)
        if(datos_nuevos):
            print(f'Se ha recibido: {datos_nuevos}')
            save.write(datos_nuevos)
            print("Escribiendo archivo")
        else:
            break

