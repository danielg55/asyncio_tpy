import asyncio

from async_socket import Socket


async def handle_echo(reader, writer):
    with Socket(reader, writer) as socket:
        message = await socket.recv(100)
        print(f"Received {message} from {socket.addr}")

        print('sleeping...')
        await asyncio.sleep(1)

        print(f"Send: {message!r}")
        await socket.send(message)


async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
