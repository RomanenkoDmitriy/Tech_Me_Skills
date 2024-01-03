from room import Room
from maze import Maze
from player import Player


def main():
    room1 = Room("Room 1")
    room2 = Room("Room 2")
    room3 = Room("Room 3")
    room4 = Room("Room 4")
    room5 = Room("Room 5")
    room6 = Room("Room 6", True)

    room1.add_door(room2)
    room1.add_door(room3)
    room3.add_door(room4)
    room3.add_door(room1)
    room4.add_door(room5)
    room4.add_door(room6)

    player = Player("User", room1)

    while True:
        if player.location.fin:
            print("Congratulations!!!")
            break

        print("Select a door:")
        for i, door in enumerate(player.location.doors):
            print(i + 1, f"Door {i + 1}")
        print(len(player.location.doors) + 1, "Back")
        resp = int(input())

        if resp <= len(player.location.doors):
            player.enter_room(player.location.doors[resp - 1].in_room)
        elif resp >= len(player.location.doors) + 1:
            player.go_back_room()



        player.look_around()


if __name__ == "__main__":
    main()
