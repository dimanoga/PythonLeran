import asyncio
import time


async def get_user_info(user_id):
    await asyncio.sleep(0.2)
    print(user_id)


if __name__ == "__main__":
    start = time.time()
    ioloop = asyncio.get_event_loop()
    tasks=[]
    for user in range(10000):
         tasks.append(ioloop.create_task(get_user_info(user)))
    wait_task= asyncio.wait(tasks)
    ioloop.run_until_complete(wait_task)
    ioloop.close()
    print(time.time() - start)
