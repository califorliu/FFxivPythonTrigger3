from ctypes import *

head_marking_interface = CFUNCTYPE(c_ubyte, c_int64, c_ubyte, c_uint)

head_marking_names = ['', 'attack1', 'attack2', 'attack3', 'attack4', 'attack5',
                      'bind1', 'bind2', 'bind3', 'stop1', 'stop2', 'square',
                      'circle', 'cross', 'triangle']

head_markings = {head_marking_names[i]: i for i in range(len(head_marking_names))}


class HeadMark(object):
    def __init__(self, head_marking_address: int, marking_controller_address: int):
        self._original = head_marking_interface(head_marking_address)
        self.marking_controller_address = marking_controller_address

    def original(self, mark_type: str, target_actor_id: int):
        """
        '', 'attack1', 'attack2', 'attack3', 'attack4', 'attack5', 'bind1',
        'bind2', 'bind3', 'stop1', 'stop2', 'square','circle', 'cross', 'triangle'
        """
        return self._original(self.marking_controller_address, head_markings[mark_type], target_actor_id)

    def __call__(self, mark_type: str, target_actor_id: int):
        """
        '', 'attack1', 'attack2', 'attack3', 'attack4', 'attack5', 'bind1',
        'bind2', 'bind3', 'stop1', 'stop2', 'square','circle', 'cross', 'triangle'
        """
        return self.original(mark_type, target_actor_id)
