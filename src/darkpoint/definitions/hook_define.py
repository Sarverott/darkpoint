""" DarkPoint: technomantic memories framework for mnemonic forrests in darkness """

#import numpy
from darkpoint.definitions.point_define import Point
from darkpoint.definitions.handler_define import Handler

class Hook:
    def __init__(self, label):
        self.name = label
        self.stack = list()

    def __iadd__(self, used_item):      # Hook() += used_item
        if isinstance(used_item, Point): # Hook() += Point()
            if used_item in self.stack:
                self.stack.remove(used_item)  # if Point() in Hook() THEN move to front
            self.stack.append(used_item)
        elif isinstance(used_item, Hook):  
            self.stack.extend(used_item.stack)  # Hook() + plugged_hook
    
    def __isub__(self, used_item):          # Hook() -= used_item
        if isinstance(used_item, Point):    # Hook() -= Point()
            if used_item in self.stack:
                self.stack.remove(used_item)    # if Point() in Hook() THEN move to back
            self.stack.insert(0, used_item)
        elif isinstance(used_item, Hook):    
            self.stack = used_item.stack.extend(self.stack)    # plugged_hook + Hook()

    def __truediv__(self, n):      # Hook() / 0 == last_hooked
        return self.stack[-1-n]   # Hook() / n == n place before last_hooked

    def __floordiv__(self, n):    # Hook() // 0 == first_hooked
        return self.stack[0+n]   # Hook() // n == n place after first_hooked

    def __mul__(self, handling_strategy):
        return Handler(self, handling_strategy)