
class Door:

    def __init__(self, per_room: object, in_room: object, lock: bool):

        self.per_room: object = per_room
        self.in_room: object = in_room
        self.lock = lock

    def go_room(self):
        return self.in_room


