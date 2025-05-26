""" DarkPoint: technomantic memories framework for mnemonic forrests in darkness """

import lark
import ast
import tokenize
import hashlib
import zlib
import json


from darkpoint.definitions.context_define import Context
from darkpoint.definitions.point_define import Point
from darkpoint.definitions.hook_define import Hook
from darkpoint.definitions.scope_define import Scope


strategies = [
    "syntax patterns eval",
    "referal links",
    "meaning tokenization",
    "memory snapshot storage",
    "triangulum coords",
    "sql database exchanges",
    "universal library traversal",
    ""
]


class Handler:


    def proxy(self, )

    def __init__(self, handling_item, strategy):
        self.item = handling_item
        self.strategy = strategy
        #pass

    def __mul__(self, handling_strategy):
        return Handler(self, handling_strategy)


