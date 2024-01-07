class Door:

    def __init__(self, per_room: object, in_room: object, lock: bool = False):
        self.per_room: object = per_room
        self.in_room: object = in_room
        self.lock = lock

    @classmethod
    def from_dict(cls, dict_door: dict):
        obj = cls(per_room=None, in_room=None, lock=False)
        for key, val in dict_door.items():
            setattr(obj, key, val)
        return obj

