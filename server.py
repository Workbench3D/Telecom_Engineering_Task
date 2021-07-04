import re
import socket


serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 53210))
serv_sock.listen(10)

while True:
    client_sock, client_addr = serv_sock.accept()
    print(f'Connected by {client_addr}')

    while True:
        data = client_sock.recv(1024)
        data = str(data)
        if re.search(r'\d{4}\s\w\d\s\d{2}:\d{2}:\d{2}.\d{3}\s\d{2}\SCR\S', data):
            if int(data[23:25]) == 00:
                chest_number = data[2:6]
                cutoff = data[7:9]
                time = data[10:18]
                print(f'Спортсмен, нагрудный номер {chest_number} прошёл отсечку {cutoff} в {time}')

            with open('run_info.txt', 'a') as file:
                file.write(data[2:25] + '\n')

        if not data:
            break

    client_sock.close()

# 0002 C1 01:13:02.877 00[CR]
