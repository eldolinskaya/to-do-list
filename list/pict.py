import asyncio #делает корутину
import aiohttp
import time
URL='http://loremflickr.com/320/240'

async def get_pic(url, session):
    async with session.get(url, allow_redirects=True) as r:
        data=await r.read() #происходит асинхронно
        name=str(time.time()) + '.png'
        save_file(data, name)

def save_file(data, name):
    with open(name, 'wb') as f:
        f.write(data)

async def main(cycles):
    tasks = []
    async with aiohttp.ClientSession() as s:
        for _ in range(cycles):
            task = asyncio.create_task(get_pic(URL, s))
            tasks.append(task)
        await asyncio.gather(*tasks) #распаковка списка

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main(10))
    print(time.time()- start)
