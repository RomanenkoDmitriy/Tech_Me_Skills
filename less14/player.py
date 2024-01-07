
class Player:

    def __init__(self, name: str, start: object):

        self.name: str = name
        self.location: object = start
        self.previous_room = None
        self.way: list = [start]
        self.hp = 0
        self.inventory = 0

    def look_around(self):
        print(self.location)
        for i, d in enumerate(self.location.doors):
            print(f"Dor {i + 1}")

    def enter_room(self, room: object):
        self.previous_room = self.location
        self.location = room
        self.way.append(room)

    def go_back_room(self):
        self.location = self.way[-2]

    def max_hp(self, hp: int):
        self.hp = hp

    def get_key(self, room_key):
        if room_key:
            self.inventory += 1
