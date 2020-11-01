from app import app


if __name__ == "__main__": 
    app.run()

'''
import asyncio

server = app
loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(server.run())
finally:
    loop.close()
'''