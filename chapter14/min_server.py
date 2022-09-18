import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9090))
s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    st = 'Thank you for connecting'
    byt = st.encode()
    c.send(byt)
    c.close()
