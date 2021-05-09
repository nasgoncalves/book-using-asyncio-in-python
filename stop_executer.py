import time
import asyncio
from concurrent.futures import ThreadPoolExecutor as Executor

async def main():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking)

    try:
        print(f'{time.ctime()} Hello!')
        await asyncio.sleep(1.0)
        print(f'{time.ctime()} Goodbye!')
    finally:
        await future

def blocking():
    time.sleep(2.0)
    print(f"{time.ctime()} Hello from a thread!")

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye!')

asyncio.run(main())