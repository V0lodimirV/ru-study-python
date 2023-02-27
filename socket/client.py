import socket
import threading

HOST = "localhost"
PORT = 8000


def receive_message(sock):
    """
    Получение сообщений от сервера
    """
    while True:
        try:
            data = sock.recv(1024)
            print(data.decode())
        except:
            print("Сервер недоступен")
            break


def start_client():
    """
    Запуск клиента
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        name = input("Введите ваше имя: ")
        s.send(name.encode())
        threading.Thread(target=receive_message, args=(s,)).start()
        while True:
            message = input("")
            if message == ":q":
                s.close()
                break
            else:
                s.send(message.encode())


if __name__ == "__main__":
    start_client()
