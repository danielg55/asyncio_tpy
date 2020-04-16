import asyncio

from async_socket import Socket


async def tcp_echo_client(message):
    with await Socket.create('127.0.0.1', 8888) as socket:
        print(f'Send: {message}')
        await socket.send(message)

        data = await socket.recv(100)
        print(f'Received: {data}')


if __name__ == '__main__':
    asyncio.run(tcp_echo_client('hey'))
