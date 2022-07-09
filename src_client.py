#!/usr/bin/env python
from lib.battery import Battery
from lib.speed import Speed
import asyncio
# get script args
import sys

if __name__ == '__main__':
    # change this to http://localhost:8080 if you are running the server locally
    bat = Battery('https://bot.rchat.fun')
    spd = Speed('https://bot.rchat.fun')
    if sys.argv[1] == 'battery':
        asyncio.run(bat.start())
    elif sys.argv[1] == 'speed':
        asyncio.run(spd.start())
    else:
        print('Usage: python src_client.py battery|speed')
        sys.exit(1)
