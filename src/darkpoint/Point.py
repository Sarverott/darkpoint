#from . import helpers

class Point:

    ROOT = None

    def __init__(self, data, context):
        if Point.ROOT is None:
            Point.ROOT=self
        self.data = data
        self.context = context
        self.hooks = {}
        self.hook_name_buffer = context 

    def __str__(self): 
        return self.data
    
    ##def __repr__(self):
        ##return f"<\"{helpers.soft_string(self.data)}\"-{self.context};{}

    def __getitem__(self, key):
        return self.hooks[key]

    def __setitem__(self, key, data):
        self.hooks[key] = Point(data, self.context)

    def __mul__(self, hook_name):
        ##if s
        self.hook_name_buffer = hook_name # setting hook name
        return self # Return self for chaining

    def __add__(self, point_to_hook):
        if self.hook_name_buffer is not None and isinstance(point_to_hook, Point):
            self.hooks[ self.hook_name_buffer ] = point_to_hook # setting point on hook
            self.hook_name_buffer = self.context # context as default hook_name_buffer
            return point_to_hook # Return hooked point for chaining
        else:
            raise ValueError(f"Point's hook_name_buffer can't be None!!!")

    def __iter__(self):
        return iter(self.hooks.items()) 

    def __truediv__(self, new_context):
        self.context = new_context  # Change current context
        return self  # Return self for chaining

    def change_context_recursively(self, new_context, old_context):
        print(f"### POINT // ###")
        print("\t", self)
        print(f"\t?-{self.context} == {old_context}")
        if self.context == old_context:
            print(f"\t\tchange context from {old_context} to {new_context}")
            self / new_context
            for hook_name, hooked_point in self:
                print(f"\t\t...asking point hooked on {hook_name}")
                hooked_point.change_context_recursively(new_context, old_context)
            return True
        else:
            print("\t\tno context change")
            return False

    def __floordiv__(self, new_context):
        if self.context != new_context: # infinite loop check
            self.change_context_recursively(new_context, self.context) # submethod
        return self
                
                
