# Skeleton Python Code for Mail Client
from socket import *
import ssl
import base64
import time

msg = "\r\n Jika anda menerima email ini, artinya SMTP dengan Python berhasil"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g Googleemailserver) and call it mail server
# Fill in start
mailserver = ("smtp.gmail.com", 465)
# Fill in End

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket, ssl_version = ssl.PROTOCOL_SSLv23)
clientSocket.connect(mailserver)
# Fill in end

recv = clientSocket.recv(1024)
print(recv)
if recvl.decode()[:3] !='220':
    print("220 reply not received from server.")

# Send HELO command and print server response.
heloCommand = "HELO Alice\r\n"
ClienSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1.decode()[:3] !='250':
    print("250 reply not receive from server.\n")

# Info for username and password
username = "harryramadhan44@gmail.com"
password = ""
base64_str = ("\x00" + username + "\x00" + password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN".encode() + base64_str + "\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = "Mail FROM: <harryramadhan@gmail.com>\r\n"
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024)
print("After MAIL FROM command: " + recv2.decode())
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptToCommand = "RCPT TO: <harryra150102@gmail.com>\r\n"
clientSocket.recv(1024)
recv3 = clientSocket.rscv(1024)
print("After RCPT TO command: " + recv3.decode())
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024)
print("After DATA command: " + recv4.decode())
# Fill in end

# Send message data.
# Fill in start for to
to = "To: <harryramadhan44@gmail.com>\r\n\r\n"
clientSocket.send(to.encode())
# Fill in end

# Fill in start for subject
subject = "Subject: Kuliah Jaringan Komputer\r\n\r\n"
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024)
print("Response after sending message body: " + recv6.decode())
# Fill in end

# Send QUIT command and get server response.
# Fill start
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv7 = clientSocket.recv(1024)
print(recv7.decode())
clientSocket.close()
# Fill in end




