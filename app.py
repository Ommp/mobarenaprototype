from sre_constants import SUCCESS
from unicodedata import name

import database

player_health = 20
player_damage =  2

class Arena:
    def __init__(self, name):
        self.name = name

    p1 = []
    p2 = []
    lobby = []
    arena = []
    spec = []
    leave = []

def create_arena(name):
    database.insert_arena(name)

def set_warp(warp_type, arena_name, x, y, z):
    database.insert_warp(warp_type, arena_name, x, y, z)

user_input = input("enter command: ")

if (user_input == "create"):
    arena_name = input("Enter arena name")
    create_arena(arena_name)

if (user_input == "setwarp"):
    warp_type = input("enter warp type (lobby, arena, spec, exit): ")
    arena_name = input("Enter arena name: ")
    x = input("enter x")
    y = input("enter y")
    z = input("enter z")
    set_warp(warp_type, arena_name, x, y, z)


if (user_input == "createclass"):
    class_name = input("Enter class name: ")
    helmet = input("Enter helmet: ")
    chest = input("Enter chestplate: ")
    leggings = input("Enter leggings: ")
    boots = input("Enter boots: ")
    database.insert_class(class_name, helmet, chest, leggings, boots)

if(user_input =="play"):
    database.fetch_arenas()
    arena_name = input("Enter the name of the arena you want to join: ")
    arena = database.fetch_arena(arena_name)
    lobby = database.fetch_lobby(arena_name)
    print("You have been transported to the lobby of arena: " +  arena)
    print("Your coordinates are now x: " + str(lobby[0]) + " y: " + str(lobby[1]) + " z: " + str(lobby[2]))

    user_input = input("Type \"ready\" when you are ready. Type anything else to quit.")
    if (user_input == "ready"):
        print("You have been transported to the arena!")
    else:
        exit()


database.con.close()