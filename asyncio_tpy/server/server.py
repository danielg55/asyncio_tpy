import asyncio
from asyncio.streams import StreamReader, StreamWriter
from typing import List, Optional

from asyncio_tpy.async_socket import Socket
from asyncio_tpy.server.user import User


class MyServer(object):
    def __init__(self):
        self.users: List[User] = []

    async def handle_connection(self, reader: StreamReader, writer: StreamWriter):
        with Socket(reader, writer) as socket:
            user = await self.handle_login(socket)

            while True:
                await asyncio.sleep(1)

    async def handle_login(self, socket: Socket) -> User:
        username = await socket.recv(100)
        user = User(socket=socket, name=username)
        self.users.append(user)

        print(f"{user} has connected.")
        await user.socket.send('Login successful!\n')

        await self.broadcast_message(f'{user} has connected!\n', exclucde_user=user)

        return user

    async def broadcast_message(self, message: str, exclucde_user: Optional[User] = None):
        for user in self.users:
            if not exclucde_user or exclucde_user.addr != user.addr:
                await user.socket.send(message)


async def main():
    my_server = MyServer()
    server = await asyncio.start_server(my_server.handle_connection, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
