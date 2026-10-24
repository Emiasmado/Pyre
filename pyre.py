# obg pela preferência <3
#        https://github.com/emiasmado

import socket

print("A PyRe esta iniciando...")
print("Passa um dns que o socket vai resolver:)\n")

def resolver():
    host = input("Digite o host: ")
    if host == "":
        print("COLOCA O DNS!!")
    else:
        ip = socket.gethostbyname(host)
        print(ip)

    return

resolver()
