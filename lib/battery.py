import asyncio
import random
import time
import socketio

sio = socketio.AsyncClient(reconnection=True)


class Battery:
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
        while True:
            try:
                await self.update_battery()
                await asyncio.sleep(1)
            except RuntimeError:
                print('error')
                continue
            except KeyboardInterrupt:
                break
        await sio.wait()
        print('disconnected')

    @staticmethod
    async def update_battery():
        try:
            await sio.emit('battery_data', {
                'op': 1,
                'd': {
                    'temp': round(random.uniform(30.0, 45.0), 1),
                    'voltage': round(random.uniform(10.0, 14.0), 1),
                    # current unix time stamp
                    'time': round(time.time() * 1000)
                },
                't': 'submit'
            })
            print('battery updated')
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
    def battery_data(data):
        print('server message: ' + str(data['t']))
