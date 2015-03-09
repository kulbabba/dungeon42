#!/usr/bin/python

import sys

if sys.version_info.major > 2:
    # For python 3 and up
    dun_input = input
else:
    # Python 2
    dun_input = raw_input

class Player:
    # HP - health ponts
    hp = 100
    max_hp = 100
    position = 0
    
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

class Screen:
    def __init__(self, msg, act, action_cb):
        print('Class init')
        self.msg = msg
        self.act = act
        self.action = action_cb

o_mapMainCorridorBegin = 1
o_mapMainCorridorEnd   = 2

def baction(u_input, player):
    print("User Input: " + str(u_input))
    if u_input == 1:
        player.set_position(o_mapMainCorridorEnd) 
    else:
        print('Some other action')

o_mapMainCorridorBegin = Screen(
"""You're standing in a long corridor,
There's a two doors:
the one on the left, and the one on the right""",

"""1. Go forward.
2. Do something.
3. Chill out!""",

baction
)

def eaction(u_input, player):
    print("User Input: " + str(u_input))
    if u_input == 1:
        player.set_position(o_mapMainCorridorBegin) 
    elif u_input == 3:
        player.die()
    else:
        print('Some other action')
        sys.exit(0)

o_mapMainCorridorEnd = Screen(
"""You have reached the end of a long corridor,
you have door in front of you, and a door on the right.""",

"""1. Go back.
2. Do something.
3. Die!""",

eaction
)

#-----------------------

mapMainCorridorEnd = Screen("scr4", "1 2 3", baction)
mapFirstRoom = Screen("scr2", "1 2 3", baction)
mapClosedDoor = ("The door is closed")

def begin_action(u_input, player):
    print("" + str(u_input))
    if u_input == 1:
        player.set_position(mapFirstRoom)
    elif u_input == 3:
        player.set_position(mapMainCorridorEnd)
    elif u_input == 2:
        print("the door is closed")

mapMainCorridorBegin = Screen(
    "You see a long dark corridor in front of you. There are  two doors. \n One is located on the right, the other is located on the left", 
    """1. Open the door on the left
2. Open the door on the right
3. Go ahead through the corridor""",
begin_action)

def main():
    player = Player(mapMainCorridorBegin) # Put player to default position
    
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

#its just a comment. Hallo Phil;)
