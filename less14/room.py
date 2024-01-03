from door import Door


class Room:
    all_rooms = []

    def __init__(self, name: str, fin: bool = False):
        self.id = len(Room.all_rooms)
        self.name: str = name
        self.doors: list[Door] = []
        self.fin: bool = fin
        Room.all_rooms.append(self)

    def add_door(self, room):
        dor = Door(self, room)
        self.doors.append(dor)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def show_doors(self):
        for dor in self.doors:
            print(dor)
