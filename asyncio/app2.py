import asyncio
import random
import time

import aiohttp
import requests


async def get_number_info(count, number):
    print(f'start {count} request  for number {number}')
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://numbersapi.com/{number}') as resp:
            response = await resp.text()
            print(f'got {count} response : {response}')


def main():
    start = time.time()
    tasks = [get_number_info(i, random.randint(1, 10000)) for i in range(1, 10)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(f'all process time {time.time() - start}')





def sync_get_number(count, number):
    print(f'start {count} request  for number {number}')
    response = requests.get(f'http://numbersapi.com/{number}')
    print(f'got {count} response : {response.text}')


def sync_main():
    start = time.time()
    for i in range(1, 10):
        sync_get_number(i, random.randint(1, 10000))
    print(f'all process time {time.time() - start}')

main()