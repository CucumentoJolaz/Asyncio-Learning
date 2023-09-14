import asyncio


async def main():
    await asyncio.sleep(2)
    print('hello')

asyncio.run(main())