from door import Door


class Room:
    all_rooms = []

    def __init__(self, name: str, fin: bool = False, key: bool = False):
        self.id = len(Room.all_rooms)
        self.name: str = name
        self.doors: list[Door] = []
        self.fin: bool = fin
        self.key: bool = key
        self.previous_room = None
        Room.all_rooms.append(self)

    def add_door(self, room, lock: bool = False):
        dor = Door(self, room, lock)
        self.doors.append(dor)
        room.previous_room = self

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def show_doors(self):
        for dor in self.doors:
            print(dor)
        if self.key:
            print("Key!")

    @classmethod
    def from_room(cls, dict_room: dict):
        obj = cls(name="", fin=False, key=False)
        for key, val in dict_room.items():
            setattr(obj, key, val)
        return obj

