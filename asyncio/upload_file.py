import asyncio
import os
import time

import aiohttp

URL = 'http://httpbin.org/post'


def get_images(path):
    files = []
    for filename in os.listdir(path):
        file = open(path + '/' + filename, 'rb').read()
        files.append(file)
    return files


async def upload_files(url, file):
    async with aiohttp.ClientSession() as session:
        await session.post(url, data=file)


async def main():
    start = time.time()
    tasks = []
    for file in get_images('images'):
        tasks.append(upload_files(URL, file))
    await asyncio.gather(*tasks)

    print(time.time() - start)


if __name__ == '__main__':
    asyncio.run(main())
