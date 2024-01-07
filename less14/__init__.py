from random import choice
from room import Room
from player import Player
from auxiliary_functions import add_dict
from my_dekor import TestDekor


room1 = Room("Room 1")
room2 = Room("Room 2", key=True)
room3 = Room("Room 3")
room4 = Room("Room 4")
room5 = Room("Room 5")
room6 = Room("Room 6", True)

room1.add_door(room2)
room1.add_door(room3)
room3.add_door(room4)
room4.add_door(room5)
room4.add_door(room6, True)


dekor = TestDekor()

@dekor.time_game
def main():
    player = Player("User", choice(Room.all_rooms))
    player.hp = len(Room.all_rooms)

    while True:
        if player.location.fin:
            print("Congratulations!!!")
            break

        if player.hp <= 0:
            print("You loos!!!!!")
            break

        player.look_around()

        print("Select a door:")
        for i, door in enumerate(player.location.doors):
            print(i + 1, f"Door {i + 1}")
        print(len(player.location.doors) + 1, "Back")
        resp = int(input())

        if resp <= len(player.location.doors):
            door = player.location.doors[resp - 1]
            room = door.in_room
            if not door.lock:
                player.enter_room(door.in_room)
                player.hp -= 1

                player.get_key(room.key)
            else:
                if player.inventory:
                    player.enter_room(door.in_room)
                    player.inventory -= 1
                    player.hp -= 1
                    player.get_key(room.key)
                else:
                    print("Need a key")

        elif resp >= len(player.location.doors) + 1:
            player.location = player.location.previous_room
            player.hp -= 1

        print(player.hp, player.inventory)




if __name__ == "__main__":
    dekor.start()
    # main()

