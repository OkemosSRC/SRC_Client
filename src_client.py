#!/usr/bin/env python
from lib.battery import Battery
import asyncio
if __name__ == '__main__':
    bat = Battery('https://bot.rchat.fun')
    asyncio.run(bat.start())
