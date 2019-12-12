# Labyrinth Adventure by Erik Follette
# COGS 18 Final Project

class Room():
    """
    Class for Labyrinth rooms. 

    ...
    Methods
    __init__(self, name, description, north, south, east, west, kills=False, treasure=False, deathMessage='')
        Create a labyrinth room that contains the room's name, description, the rooms
        that connect to it, whether the room will kill the player, and whether it 
        contains the treasure.

    """

	# Constructor
    def __init__(self, name, description, north, south, east, west, kills=False, treasure=False, deathMessage=''):
        """labyrinth room constructor.
        
        Parameters
        ----------
        name : string
            Name or title of the room. Ex: "bedroom"
        description: string 
            Description of the room. Ex: "A room with a bed in items"
        north : string 
            Name of room that will be entered if the player goes North
        south : string 
            Name of room that will be entered if the player goes South
        east : string 
            Name of room that will be entered if the player goes East
        west : string
            Name of room that will be entered if the player goes West
        kills : Boolean
            Whether or not the player will be killed by this room. Default: False
        treasure : Boolean
            Whether or not the treasure is in the room. Default: False
        deathMessage : string
        Message that describes the death of the player. Ex: "You are killed by a rock" 
            Default: '' (empty string)
            
        """
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.kills = kills
        self.treasure = treasure
        self.deathMessage = deathMessage
        
