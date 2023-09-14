import asyncio
import random

async def coroutine1(queue, event):
    sendings_num = 5
    print('Coroutine 1 started...')
    while sendings_num:
        # Perform some work in a loop
        #print('Coroutine 1 is working...')
        await asyncio.sleep(1)

        # Randomly send a message
        if random.randint(0,1) == 1:
            print('Coroutine 1 is sending a message...')
            await asyncio.sleep(0)
            sendings_num -= 1
            # Add the message to the queue
            await queue.put('Message from coroutine 1')

    # Set the event when all messages have been sent
    event.set()
    print('Coroutine 1 finished its job! All messages have been sent.')

async def coroutine2(queue, event):
    print('Coroutine 2 started...')
    while True:
        # Wait for a message to arrive in the queue
        message = await queue.get()
        # Process the message
        print('Coroutine 2 received message: {}'.format(message))
        # Perform some work with the message
        print('Coroutine 2 is doing some work...')
        await asyncio.sleep(random.randint(1, 3))
        print('Coroutine 2 is done!')

        # Check if all messages have been sent and processed
        if event.is_set():
            break

    print('Coroutine 2 finished its job! All messages have been accepted and evaluated.')

async def main():
    # Create a queue for message passing
    queue = asyncio.Queue()
    # Create an event to signal when all messages have been sent and processed
    event = asyncio.Event()

    # --------- run as tasks ------------------
    # task1 = asyncio.create_task(coroutine1(queue, event))
    # task2 = asyncio.create_task(coroutine2(queue, event))
    #

    # tasks = [task1, task2]
    # done, pending = await asyncio.wait(
    #     tasks, return_when=asyncio.ALL_COMPLETED)

    # --------- run as futures ------------------
    # coroutines = [coroutine1(queue, event), coroutine2(queue, event)]
    # future1 = asyncio.ensure_future(coroutine1(queue, event))
    # future2 = asyncio.ensure_future(coroutine2(queue, event))
    #
    # futures = [future1, future2]
    # done, pending = await asyncio.wait(
    #     futures, return_when=asyncio.ALL_COMPLETED)

    # ---------- gather coroutines in asyncio.gather and combine in single future -------------------
    coroutines = [coroutine1(queue, event), coroutine2(queue, event)]
    single_future = await asyncio.gather(
        *coroutines
    )

    print("End of program!")

asyncio.run(main())

asyncio.run(main())