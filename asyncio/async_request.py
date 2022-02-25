import time

import aiohttp
import asyncio

import requests


def get_pic(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    start = time.time()
    url = 'https://loremflickr.com/320/240'
    for i in range(0, 10):
        write_file(get_pic(url))

    print(time.time() - start)


#if __name__ == '__main__':
   # main()


###################################################

def write_image(data):
    filename = 'file-{}.jpeg'.format((int(time.time() * 1000)))
    with open(filename, 'wb') as file:
        file.write(data)


async def async_get_pic(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def async_main():
    url = 'https://loremflickr.com/320/240'
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(0, 10):

            tasks.append(async_get_pic(url, session))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(async_main())
    print(time.time() - start)
