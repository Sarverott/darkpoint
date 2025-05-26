"""DarkPoint: technomantic memories framework for mnemonic forrests in darkness"""

import threading
import subprocess
import os
import time
import zlib

#__all__ = ["Context"]

from darkpoint.definitions.handler_define import Handler

class Context():
    def __init__(self, title, point):
        self.labels = [zlib.adler32(title)]
        self.name = title
        self.data = {
            "AT":time.time()
        }
        self.point = point

    def __mul__(self, handling_strategy):
        return Handler(self, handling_strategy)