import asyncio
import asyncio
from asyncio import StreamWriter, StreamReader

async def send_event(msg: str):
    await asyncio.sleep(1)

async def echo(reader: StreamReader, writer: StreamWriter):
    print('New connection')

    try:
        while data := await reader.readline():
            writer.write(data.upper())
            await writer.drain()

        print('Leaving connection',)
    except asyncio.CancelledError:
        msg = 'Connection dropped!'
        print(msg)
        asyncio.create_task(send_event(msg))

async def main(host='127.0.0.1', port=8888):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Bye!')
