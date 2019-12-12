# import labyrinth room
from adventureGame import room as r

# Rooms for the test game
testRooms = {
    'empty': r.Room( 'are in the first chamber of the labyrinth, an empty room', 
                  'The stone floors and walls are cold and damp. There are three doorways, one on each wall.', 
                  'temple', None, 'torture', 'bedroom'
                  ),
    'temple': r.Room( 'are in a temple', 
                  'In the center of the room, the treasure you have been seeking lies atop an ornate dais.', 
                  None, 'empty', None, None, treasure=True
                  ),
    'torture': r.Room( 'are in a torture chamber', 
                  'There are no doors except for the one you just came through.', 
                  None, None, None, 'empty', kills=True, 
                  deathMessage='Suddenly, a trap activates and you are impaled. You have died :('
                  ),
    'bedroom': r.Room( 'are in a bedroom. The sheets have a light film of dust on them. No one has slept here for quite some time', 
                  'There are no doors except for the one you just came through.', 
                  None, None, 'empty', None
                  ),
        }

# Starting room for the test game
starting_room = testRooms['empty']