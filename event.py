import asyncio
import time

async def waiter(event):
    while not event.is_set():
        print('waiting ...')
        await asyncio.sleep(1)
        #time.sleep(1)
    print('... got it!')
    return 'Returned value'


async def main():
    # Create an Event object.
    event = asyncio.Event()

    # Spawn a Task to wait until 'event' is set.
    waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 1 second and set the event.
    await asyncio.sleep(1)
    event.set()

    # Wait until the waiter task is finished.
    a = await waiter_task
    print(a)


asyncio.run(main())
