#!/usr/bin/env python

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # Private copy of original update() method
                      # Mangled to `_Mapping__update()`

class MappingSubclass(Mapping):
    def update(self, keys, values):
        # Provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

m = Mapping([1, 2, 3])
m.update([])
print(m.items_list)

ms = MappingSubclass([4, 5, 6]) # Mapping.update() is called in __init__()
ms.update(['seven', 'eight'], [7, 8]) # MappingSubclass.update() is called
print(ms.items_list)

# ms._Mapping__update([9]) # Mapping.update() can be called by mangled name
