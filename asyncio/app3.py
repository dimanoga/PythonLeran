import asyncio
import random
import time

import aiohttp
import requests


async def get_number_info(number):
    print(f'start request  for number {number}')
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://numbersapi.com/{number}') as resp:
            response = await resp.text()
            number_was = int(response[:response.find('is')])
            return number_was


async def print_results(num):
    print(f'number is: {num}')
    await asyncio.sleep(2)
    print('done printing')


async def main():
    futures = [get_number_info(random.randint(1, 10000000)) for i in range(1, 3)]
    done, _ = await asyncio.wait(futures)

    numbers = []
    for future in done:
        numbers.append(future.result())

    print_futures = [print_results(number) for number in numbers]
    await asyncio.wait(print_futures)


start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
print(time.time() - start)

##############################


def sync_get_number_info(number):
    print(f'start sync request  for number {number}')
    response = requests.get(f'http://numbersapi.com/{number}')
    response = response.text
    number_was = int(response[:response.find('is')])
    return number_was


def sync_print_results(num):
    print(f'number is: {num}')
    time.sleep(2)
    print('done printing')


def sync_main():
    numbers = []
    for i in range(1, 3):
        numbers.append(sync_get_number_info(random.randint(1, 10000000)))

    for number in numbers:
        sync_print_results(number)


start = time.time()
sync_main()
print(time.time() - start)
