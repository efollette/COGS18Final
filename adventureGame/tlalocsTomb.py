# Labyrinth by Erik Follette
# COGS 18 Final Project
from adventureGame import room as r

# Rooms for the Tlāloc's Tomb
tlalocsTombRooms = {
    '02': r.Room( 'are in front of Tlāloc\'s Tomb, final resting place of the Aztec God of Rain, and home to the legendary fountain of Tlāloc\'s Tears, the key to eternal life', 
                  'There is a stone doorway in front of you, lined with the skulls of those who dared to challenge Tlāloc in their pusuit for immortality, a reminder of whats at stake.', 
                  '12', None, None, None
                  ),
    '10': r.Room( 'walk into the next room', 
                  'In the back of the room you see it! An ornate fountain, depicting the life and deeds of Tlāloc, gurgles with the Tears of Tlāloc.', 
                  None, None, '11', None, kills=True, deathMessage='You run up to the fountain and take a drink from it. The water is cool and pleasant as it flows down your throat. You feel a tingling sensation; immortality at last! Suddenly, your heart begins to burn and you realize that the water was not what you thought it was. As your vision begins to fade, you curse the greed that brought you to an early death.'
              ),
    '11': r.Room( 'walk into the next room',
                  'This room looks identical to the one you were just in. Seems like it would be pretty easy to get lost here...',
                  '21', None, '12', '10'
              ),
    '12': r.Room( 'enter the Tomb. As soon as you enter, the doorway behind you shuts. Only one way out now: onwards', 
                  'The first room is dimly lit by an unknown light source. You see three doorways, one in each direction.', 
                  '22', None, '13', '11'
                  ),
    '13': r.Room( 'walk into the next room',
                  'This room looks identical to the one you were just in. Seems like it would be pretty easy to get lost here...',
                  '23', None, '14', '12',
                  ),
    '14': r.Room( 'walk into the next room',
                  'This room is full of plants. To your right lies a door covered in cobwebs, in front of you is a more pristine door.',
                  '24', None, '15', '13',
                  ),
    '15': r.Room( 'clear the cobwebs off the door and walk into the next room',
                  'In front of you lies a long table set up for a feast. Somehow, the food looks like it was recently prepared, it is still steaming. You are filled with hunger but wisely choose to not eat the food. There is only one door in front of you.',
                  '25', None, None, '14',
                  ),
    '21': r.Room( 'walk into the next room', 
                  'This room looks like a doctor\'s office lobby except there is no one here. To your right you see a door labeled "Glenn Marin D.D.S"; in front of you there is a door that says "Maintenance".',
                  '31', '11', '22', None
                  ),
    '22': r.Room( 'walk into the next room', 
                  'You notice what seem to be blood stains in the center of the room. Foolishly, you approach the stains to inspect them.', 
                  '32', '12', '23', '21', kills=True, deathMessage='You notice that the source of the stains is a drip coming from the ceiling. You look up, and to your horror, you realize what the source of the stains is as a gaping maw, full of razor sharp teeth, engulfs your vision and you are nore more.'
                  ),
    '23': r.Room( 'walk into the next room', 
                  'This room has a small pool with water so black it acts as a mirror. You stare at yourself, lost in your own reflection, but something causes the water to ripple and you look away. It seems like a lot of time has passed.', 
                  '33', '13', '24', '22', 
                  ),
    '24': r.Room( 'walk into the next room', 
                  'There is nothing in this room except for doorways to other rooms. You are relieved by the room\'s simplicity.', 
                  '34', '14', '25', '23', kills=True, deathMessage='Suddenly, the floor opens up beneath you and you fall into a pit of spikes. You die a slow and painful death.'
                  ),
    '25': r.Room( 'walk into the next room', 
                  'This room smells pleasant, like home. You feel motivated to find the treasure.', 
                  '35', '15', None, '24',
                  ),
    '31': r.Room( 'walk into the next room', 
                  'The floor is slick and at a steep angle. You immideately lose your footing and begin to slide towards the chasm in the center of the room.',
                  '41', '21', '32', None, kills=True, deathMessage='As you\'re sliding, a slimy tentacle bursts out of the chasm and wraps around your leg, pulling you into the center where you are devoured by the monstruosity at the bottom.'
                  ),
    '32': r.Room( 'walk into the next room', 
                  'There are doors on each side. The one in front of you is padlocked but looks like you may be able to pick it.', 
                  '42', '22', '33', '31', 
                  ),
    '33': r.Room( 'walk into the next room', 
                  'The floor is covered in moss and water drips from the ceiling.', 
                  '43', '23', '34', '32', 
                  ),
    '34': r.Room( 'walk into the next room', 
                  'The floor is lava, but you were a champion at this game in elementary school and you are able to navigate the room with ease. You see doors on all sides.', 
                  '44', '24', '35', '33', 
                  ),
    '35': r.Room( 'walk into the next room', 
                  'There is a window to your right and you notice that you are under water. The fish swim about lazily, indifferent to your struggle to find the treasure. Part of you wishes you could be out there swimming with them.', 
                  '45', '25', None, '34',
                  ),
    '41': r.Room( 'enter a room unlike any of the others. Balls of light float around you, gently illuminating the room. Vibrantly colored murals line the walls, depicting Tlāloc\'s story. There are shallow pools along the sides of the room, teeming with aquatic life.', 
                  'You walk to the end of the room where a bust of Tlāloc\'s face sits atop an ornate dais. From its eyes you notice tears running down its face.',
                  None, '31', '42', None, treasure=True
                  ),
    '42': r.Room( 'pick the lock and moonwalk into the next room, feelin\' yo self', 
                  'Upon entering, you are greeted by a crowd that cheers on your dance moves. You bust out some of your best moves but it seems that the crowd has lost interest. Dejectedly they all disappear and you are now alone in a stone room with doors on all sides.', 
                  '52', '32', '43', '41', 
                  ),
    '43': r.Room( 'open the door to walk into the next room', 
                  'A dark, rotting hand grabs you the second you open the door.', 
                  '53', '33', '44', '42', kills=True, deathMessage='You are pulled in and are grabbed by several more hands. They pull at you in many directions and you are ripped apart.'
                  ),
    '44': r.Room( 'walk into the next room', 
                  'The walls of this room are all mirrors. You see endless reflections of yourself and begin to wonder which reflection is the real you. You are able to make out doors on all sides of the room.', 
                  '54', '34', '45', '43', 
                  ),
    '45': r.Room( 'open the door to walk into the next room', 
                  'Water rushes out and the entire tomb is flooded.', 
                  '45', '25', None, '34', kills=True, deathMessage='Since the Tomb\'s entrance closed, there is no escaping this watery grave.'
                  ),
    '52': r.Room( 'enter the next room', 
                  'You step on a pressure plate and realize the end has come.', 
                  None, '42', '53', None, kills=True, deathMessage='You are hit by a poison arrow and die.'
                  ),
    '53': r.Room( 'open the door and enter the next room', 
                  'You are in pitch black darkness. Its cold and wet, the air crackles with static energy. You feel as though you have walked into a storm cloud.', 
                  None, '43', '54', '52', 
                  ),
    '54': r.Room( 'walk into the next room', 
                  'The room is filled with a blinding white light. Even closing your eyes does not shield you from the light.', 
                  None, '44', '55', '53', 
                  ),
    '55': r.Room( 'open the door and walk into the next room', 
                  'There is a hot tub in the center of the room.', 
                  None, '45', None, '54', 
                  ),
        }

# Starting room for the Tlāloc's Tomb
starting_room = tlalocsTombRooms['02']