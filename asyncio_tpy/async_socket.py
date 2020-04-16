import asyncio
from asyncio.streams import StreamReader, StreamWriter


class Socket(object):
    def __init__(self, reader: StreamReader, writer: StreamWriter):
        self._reader = reader
        self._writer = writer

    @classmethod
    async def create(cls, host: str, port: int):
        reader, writer = await asyncio.open_connection(host, port)
        return cls(reader, writer)

    async def send(self, message: str) -> None:
        self._writer.write(message.encode())
        await self._writer.drain()

    async def recv(self, size: int) -> str:
        message = await self._reader.read(size)
        return message.decode()

    def close(self):
        self._writer.close()

    @property
    def addr(self) -> str:
        return self._writer.get_extra_info('peername')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Closing the connection...')
        self.close()
