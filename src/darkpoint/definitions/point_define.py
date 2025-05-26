""" DarkPoint: technomantic memories framework for mnemonic forrests in darkness """

from darkpoint.definitions.hook_define import Hook
from darkpoint.definitions.context_define import Context
from darkpoint.definitions.handler_define import Handler
from darkpoint.definitions.scope_define import Scope

import zlib
import time


class Point:

    def __ne__(self, changescope_name):  # Point() != scopename 
        tmp = Point({"name":str(zlib.adler32(time.time())), "context":changescope_name, "scope":changescope_name})
        tmp.scope = Scope.invoke(changescope_name, tmp)
        self[changescope_name] = tmp# new Hook(scopename)
        return self[changescope_name] / 0

    def __ixor__(self, context_name):  # Point() ^= context_topic
        self.context = self.scope % context_name
        if self.context.name not in self.data:
            self.data[self.context.name] = list()

    def __ilshift__(self, data_input):  # Point() <<= informations ### will be added to context_topic list
        self.data[self.context.name].append(data_input)

    def __getitem__(self, key):         # Hook() = Point()["hookname"]
        if not key in self.hooks:
            return None
        else:
            return self.hooks[key]
        
    def __setitem__(self, key, item):    # Point()["hookname"]=Point()
        if not key in self.hooks:
            self.hooks[key] = Hook(key)    # init hook if not exist
        
        self.hooks[key] += item

    def __init__(self, setup = {"name":str(zlib.adler32(time.time())), "context":"ROOT", "scope":"temp"}):   # Point({"name":"darkness","context":"ROOT","scope":"CORE"})
        self.name = setup["name"]
        self.data = dict()
        self ^= setup["context"]
        #self.context = setup["context"]
        #self.scope = setup["scope"]

    def __mul__(self, handling_strategy):
        return Handler(self, handling_strategy).proxy

    # hooks = dict()

    # values = list()

    # viewer = None

    # current_context = None

    # def PALACE(self):
    #     global DARK
    #     DARK["return_pointer"] = Hook(self)
    #     self *= self.this_context
    #     DARK.current_context = Context(self.current_context+"background")

    # def __init__(self):
    #     pass

    # def __getitem__(self, key):
    #     return self.hooks[key]

    

    # def __add__(self, shift)

