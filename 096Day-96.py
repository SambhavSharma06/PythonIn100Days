# AsyncIO in Python!!
import asyncio

async def say_hello():
    print("Hello...")
    await asyncio.sleep(2)
    print("World!")
    
async def main():
    await asyncio.gather(
        say_hello(),
        say_hello()
    )

asyncio.run(main())
