import asyncio
import random

class AsyncInter:

    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop

    def __aiter__(self):
        self.irange = iter(range(self.start, self.stop))
        return self

    async def __anext__(self):
        try:
            # await asyncio.sleep(random.randint(1, 2))
            return next(self.irange)
        except StopIteration:
            raise StopAsyncIteration

async def main():
    async for i in AsyncInter(1, 10):
        print(i)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
