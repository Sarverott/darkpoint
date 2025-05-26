""" DarkPoint: technomantic memories framework for mnemonic forrests in darkness """


from darkpoint.definitions.hook_define import Hook
from darkpoint.definitions.context_define import Context
from darkpoint.definitions.handler_define import Handler
from darkpoint.definitions.point_define import Point


ALL_SCOPES = dict()


class Scope:

    def invoke(name, point_item):
        if name not in ALL_SCOPES:
            point_item.name = name
            return Scope(point_item)
        else:
            grabbed = ALL_SCOPES[name]
            grabbed.point_net.append(point_item)
            return grabbed

    def __init__(self, root_point):
        ALL_SCOPES[root_point.name] = self
        self.scope_contexts = dict()
        self.root = root_point
        self.point_net = [self.root]
        pass

    def __mul__(self, handling_strategy):
        return Handler(self, handling_strategy)