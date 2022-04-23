import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind(('', port))
s.listen()

conn, addr = s.accept()
print(addr, "is connected to server.")

command = input(str("Enter Command: "))
conn.send(command.encode())
print("Command has been sent successfully.")

data = conn.recv(1024)
if data:
    print("Command received and executed successfully.")


