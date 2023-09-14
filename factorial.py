import asyncio
import time

from req_http import http_get, http_get_sync


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    start = time.perf_counter()
    # Schedule three calls *concurrently*:
    pokemon_query = [http_get(f'https://pokeapi.co/api/v2/pokemon/{i + 1}') for i in range(100)]
    pokemon_query_2 = [http_get(f'https://pokeapi.co/api/v2/pokemon/{i + 1}') for i in range(100, 200)]
    L = await asyncio.gather(
        # factorial("A", 2),
        # factorial("B", 3),
        # factorial("C", 4),
        #http_get('https://pokeapi.co/api/v2/pokemon/10')
        *pokemon_query,
        *pokemon_query_2
    )

    names = ", ".join([l['name'] for l in L])
    print(names)

    print(f"Time spend on calculating, async: {time.perf_counter() - start:.1f} s")

    #
    # start = time.perf_counter()
    # L = [http_get_sync(f'https://pokeapi.co/api/v2/pokemon/{i + 1}') for i in range(200)]
    #
    # names = ", ".join([l['name'] for l in L])
    # print(names)
    #
    # print(f"Time spend on calculating, async: {time.perf_counter() - start:.1f} s")
    #


asyncio.run(main())
