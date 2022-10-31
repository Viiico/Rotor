import socket

def manageData(c, clientData):
    print(clientData)
    c.send(f"Rotororo w {clientData}".encode())

s = socket.socket()
port = 5050
s.bind(('', port))
s.listen(5)
print("socket rotorororo")
while True:
    c, addr = s.accept()
    clientData = c.recv(1024).decode()
    manageData(c, clientData)

c.close()