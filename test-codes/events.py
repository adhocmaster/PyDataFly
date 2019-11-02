import asyncio


async def aFunc():
    print("first")
    await asyncio.sleep(2)
    print("last")


async def bFunc():
    print("b first")
    await cFunc()
    await asyncio.sleep(1)
    print("b last")


async def cFunc():
    print("c first")
    await asyncio.sleep(5)
    print("c last")


# asyncio.run(aFunc())
# asyncio.run(bFunc())

async def scheduler():

    taska = asyncio.create_task(aFunc())
    taskb = asyncio.create_task(bFunc())

    await taska
    await taskb


asyncio.run(scheduler())


