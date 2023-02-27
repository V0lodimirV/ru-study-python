import socket
import threading

HOST = "localhost"
PORT = 8000

clients = set()


def handle_client(conn, addr):
    """
    Обработка сообщений от клиента
    """
    print(f"Новый клиент подключился: {addr}")
    clients.add(conn)
    while True:
        try:
            data = conn.recv(1024)
            if data:
                message = f"{addr}: {data.decode()}"
                for client in clients:
                    if client != conn:
                        client.send(message.encode())
            else:
                clients.remove(conn)
                print(f"Клиент отключился: {addr}")
                conn.close()
                break
        except:
            clients.remove(conn)
            print(f"Клиент отключился: {addr}")
            conn.close()
            break


def start_server():
    """
    Запуск сервера
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Сервер запущен на порту {PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    start_server()
