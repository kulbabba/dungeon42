#!/usr/bin/python

#
# Import declarations
#
import sys
import random

#
# Compatibility code (python 2.x / 3.x)
#
if sys.version_info.major > 2:
    # For python 3 and up
    dun_input = input
else:
    # Python 2
    dun_input = raw_input

#
# Global variables
#
chest_content_list = ["empty", "key", "undead", "money"]
chest_content_status = [True, True, True, True] # False = empty; True = full;


#
# Classes
#
class Player:
    # HP - health ponts
    hp = 100
    max_hp = 100
    position = 0
    key = 0

    def __init__(self, pos):
        self.position = pos

    def set_position(self, new_position):    
        if self.is_dead() == True:
            print("ERROR.Since you are dead, you cannot walk")
        else:
            self.position = new_position

    def get_position(self):
        return self.position

    def get_health(self):
        return self.hp

    def dec_health(self, health):
        self.hp = self.hp - health
        if self.hp < 0:
            self.hp = 0

    def inc_health(self, health):
        self.hp = self.hp + health
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def die(self):
        self.hp = 0

    def is_dead(self):
        if self.hp > 0:
            return False
        else:
            return True

    def have_key(self, keys): 
        self.key = self.key + keys

    def get_key(self):
        return self.key


class Screen:
    def __init__(self, msg, act, action_cb):
        self.msg = msg
        self.act = act
        self.action = action_cb

#=====================================

def second_room_action(u_input, player):
    print("" + str(u_input))
    if u_input == 1:
        print ("there is undead, there is a key")
        player.have_key(2)
        player.set_position(mapMainCorridorBegin)
    if u_input == 2:
        player.set_position(mapFirstRoom)


mapSecondRoom = Screen(
    "You can see a chest.",

    "1. Open a chest.\n"
    "2. Leave the room.",

    second_room_action
)

#=====================================

# TODO: Check all actions for the chests
def third_room_action(u_input, player):
    choice_index = u_input - 1
    choice = chest_content_list[choice_index]

    # Check if chest is empty
    if chest_content_status[choice_index] == False or choice == "empty":
        print("The chest is empty")

    elif choice == "undead":
        print("There is undead. He attacks you")
        player.dec_health(50)
    elif choice == "money":
        print("The chest has money")
        player.set_position(mapThirdRoom)
    elif choice == "key":
        print("You have found a key")
        player.have_key(1)
        player.set_position(mapMainCorridorBegin)

    chest_content_status[choice_index] = False


mapThirdRoom = Screen(
    "You see four chests",

    "1. Open the first one.\n"
    "2. Open the second chest.\n"
    "3. Open the third chest.\n"
    "4. Open the fourth chest.\n",

    third_room_action
)

#=====================================

def end_corridor_action(u_input, player):
    print("" + str(u_input))
    if u_input == 1:
            player.set_position(mapThirdRoom)
    elif u_input == 2:
        if player.get_key() > 1:
            print ("scr10")
        else:
            print ("the door is closed")


mapMainCorridorEnd = Screen(
    "You see one door in front of you and one door on the right.",

    "1. Open the door in front of you\n"
    "2. Open the door on the left.",

    end_corridor_action
)

#=====================================

def first_room_action(u_input, player):
    print("" + str(u_input))
    if u_input == 1:
        print("The coffin is opened. You see the undead...")
    elif u_input == 2:
        if player.get_key() > 0:
            player.set_position(mapSecondRoom)
        else:
            print("the door is closed:(")


mapFirstRoom = Screen(
    "You can see  dark room. There is coffin.There is one more door.",

    "1. Open the coffin.\n"
    "2. Open the door",

    first_room_action
)

#=====================================

def begin_action(u_input, player):
    print("" + str(u_input))
    if u_input == 1:
        player.set_position(mapFirstRoom)
    elif u_input == 3:
        player.set_position(mapMainCorridorEnd)
    elif u_input == 2:
        print("the door is closed")


mapMainCorridorBegin = Screen(
    "You see a long dark corridor in front of you. There are two doors.\n"
    "One is located on the right, the other is located on the left", 

    "1. Open the door on the left\n"
    "2. Open the door on the right\n"
    "3. Go ahead through the corridor",

    begin_action
)

#=====================================

def main():
    player = Player(mapMainCorridorBegin) # Put player to default position

    random.shuffle(chest_content_list)
    while player.get_health() > 0:
        screen = player.get_position()
        print('---\n' + screen.msg + '\n---\n\n')
        print(screen.act + '\n\n')
        i = int(dun_input())
        screen.action(i, player)

    if player.is_dead() == True:
        print("You have died a horrible death!")
    else:
        print("Congratulations!!! You have finished the game!")

if __name__ == '__main__':
     main()

