import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1024))
msg=s.recv(7)
print(msg.decode("utf-8"))