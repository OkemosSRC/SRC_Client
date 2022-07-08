import asyncio
import random
import time
import socketio
import numpy as np

sio = socketio.AsyncClient(reconnection=True)


class Speed:
    global sio

    def __init__(self, url: str):
        self.url = url

    async def start(self):
        global sio
        try:
            await sio.connect(self.url)
            await self.loop()
        except ConnectionRefusedError:
            print('connection refused')
            return False
        except KeyboardInterrupt:
            return False
        except Exception as es:
            print(es)
            print("Retrying in 5 seconds...")
            time.sleep(5)
            await self.start()

    async def loop(self):
        counter = 0
        while True:
            try:
                await self.update_speed(counter)
                counter += 0.1
                await asyncio.sleep(0.1)
            except RuntimeError:
                print('error')
                continue
            except KeyboardInterrupt:
                break
        await sio.wait()
        print('disconnected')

    @staticmethod
    async def update_speed(ins):
        try:
            await sio.emit('speed_data', {
                'op': 1,
                'd': {
                    'speed': round(np.sin(ins) * 10 + 40 + random.uniform(-3.0, 3) * random.uniform(-1.0, 1.0), 1),
                    # current unix time stamp
                    'time': round(time.time() * 1000)
                },
                't': 'submit'
            })
            # print('speed updated')
        except KeyboardInterrupt:
            return False
        except Exception as excepts:
            if str(excepts) == '/ is not a connected namespace.':
                print('server disconnected')
            else:
                print(excepts)

    @staticmethod
    async def stop():
        await sio.disconnect()

    @staticmethod
    @sio.event
    async def disconnect():
        print('disconnected from server')

    @staticmethod
    @sio.event
    def speed_data(data):
        pass
        # print('server message: ' + str(data['t']))
