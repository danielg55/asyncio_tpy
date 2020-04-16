import asyncio
from dataclasses import dataclass

from asyncio_tpy.async_socket import Socket


@dataclass
class User:
    socket: Socket
    name: str

    @property
    def addr(self) -> str:
        return self.socket.addr

    def __str__(self) -> str:
        return f'<{self.__class__.__name__}: {self.name}, {self.addr}>'


async def a():
    print('start')
    await asyncio.sleep(1)
    print('finish')


async def main():
    asyncio.create_task(a())
    asyncio.create_task(a())
    asyncio.create_task(a())


if __name__ == '__main__':
    asyncio.run()
