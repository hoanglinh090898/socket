import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen(5)
while True:
    ctl, adr=s.accept()
    print(f"connection to {adr} ")
    ctl.send(bytes("Socket Programming in Python", "utf-8"))