import asyncio

from asyncio_tpy.async_socket import Socket


class Client:
    def __init__(self, socket: Socket):
        self._socket = socket

    @classmethod
    async def create(cls, host: str, port: int):
        return cls(await Socket.create(host, port))

    async def start(self):
        def _listen():
            while True:
                pass

        await asyncio.create_task(_listen())

    async def login(self, username):
        pass


async def tcp_echo_client(username: str):
    with await Socket.create('127.0.0.1', 8888) as socket:
        await socket.send(username)

        while True:
            data = await socket.recv(100)
            print(f'Received: {data}')


if __name__ == '__main__':
    for i in range(10):
        from multiprocessing import Process

        Process(target=asyncio.run, args=(tcp_echo_client(str(i)),)).start()
