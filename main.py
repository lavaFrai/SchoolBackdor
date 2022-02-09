import os
import socket

while True:
    try:
        sock = socket.socket()
        sock.bind(('', 12321))
        sock.listen(1)
        conn, addr = sock.accept()
        conn.send(b"Success connected!\n")
        conn.send(b"Enter the password:\n $> ")
        data = conn.recv(2048)
        if data.decode('utf8') == "asdzxc12\n":
            while True:
                data = conn.recv(2048)
                command = data.decode("utf8").replace('\n', '').split()[0]
                args = data.decode("utf8").replace('\n', '').split()[1:]
                print(command, args)
                if command == "reboot":
                    conn.send(b"Ok, rebooting\n")
                    os.system("shutdown -r -t 0")
        else:
            conn.send(b"Invalid!\n")
            conn.close()
    except BaseException:
        pass
