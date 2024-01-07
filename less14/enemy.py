
class Enemy:

    def __init__(self, name: str, start: object):
        self.name = name
        self.location = start
        self.previous_room = None

    def enter_room(self, room):
        self.previous_room = self.location
        self.location = room
