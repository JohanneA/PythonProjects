#["U", "D", "L", "R"]
#{ "D":room1}
# {"L":room5, "R":room3, "U":room2, "D":room4}
class Room:
    name = ""
    description = ""
    joining_rooms = {}


def create_room(name, description):
    new_room = Room()
    new_room.name = name
    new_room.description = description
    return new_room


room1 = create_room("Cold room", "You're standing in a super cold room with an interesting ice sculpture in the middle. "
                                 "It looks like a dog. Much wow, such art.")
room2 = create_room("Jungle Room", "Wooow, it seems like you walked into a jungle consisting of two palmtrees. "
                                   "A sloth is sleeping on trunk, best not distub it.")
room3 = create_room("Rocky Room", "So many rock guitars and speakers everywhere. Is that Nickelback playing in the background?")
room4 = create_room("Couch Room", "If you need a break, this is the place to rest up. Couches all around and big screen TV's, "
                                  "such a shame it only seems to be playing Love Island")
room5 = create_room("Food Room", "WATCH OUT!! You almost stepped in whipped cream!! Do you now how hard that is to make!? "
                                 "It's probably a better idea to walk around the outside, the middle looks a little cakey")
room6 = create_room("Dark Room", "It's a bit dark in here, maybe you should turn on the lights")
room1.joining_rooms =  {"L":room5, "R":room3, "U":room2, "D":room4}
room2.joining_rooms =  {"D":room1}
room3.joining_rooms =  {"L":room1}
room4.joining_rooms =  {"R":room6, "U":room1}
room5.joining_rooms =  {"R":room1}
room6.joining_rooms =  {"L":room4}

current_room = room1
playing = True
user_input = input("Do you want to play the adventure of a lifetime game? Y or N ")
if user_input == 'Y':
    while playing:
        print(current_room.name)
        print(current_room.description)
        input_direction = input("What do you want to do now? Type in a direction you want to go in (U,D,L,R) ")
        if input_direction in current_room.joining_rooms:
            current_room = current_room.joining_rooms[input_direction]
        else:
            still_playing = input("It seems like you can't go that way. Do you want to continue playing? Y or N ")
            playing = still_playing != 'N'

        print(" ")