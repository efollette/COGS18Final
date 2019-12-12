# Labyrinth Adventure by Erik Follette
# COGS 18 Final Project

class AdventureGame():
    """
    Class to load the Labyrinth rooms and run the game using those rooms.

    ...
    Attributes
    ----------
    instructions : string
        Instructions on how to play the game
    directions : Dictionary{ string: string{} }
        Dictionary containing 4 keys one for each direction. Each key maps to  
        an array of accepted words for that key's direction.
    keep-playing : Dictionary{ string: string{} }
        Dictionary containing keys for 'yes' and 'no' which map to an array of 
        strings that mean 'yes' or 'no'

    Methods
    -------
    __init__(self, rooms, startingRoom)
        Create an adventureGame object that is capable of being played.
    playGame(self)
        Play the game that is defined by the rooms of the adventureGame that calls it.

    """
    
	# Instructions on how to play the game
    instructions = ('In this game, you take the role of a treasure ' 
    'hunter navigating a dangerous maze of rooms in the hopes of finding the legendary Tlāloc\'s Tears. ' 
    'To play this game, simply type a directional command to navigate through the rooms. The directions are: \n' 
    '\t To go to the room ahead of you: forward, forwards, north, n, f \n' 
    '\t To go to the room behind you: backwards, backward, back, south, s, b \n' 
    '\t To go to the room to your left: left, west, w, l \n' 
    '\t To go to the room to your right: right, east, e, r \n'
    '\t To quit: q, quit, exit, end \n'
    'Be careful, and good luck trying to find the treasure!')
    
	# Dictionary of acceptable directions and their variants
    directions = {'1': {'north', 'forward', 'forwards', 'f', 'n',},
                  '2': {'south', 'backwards', 'backward', 'back', 's', 'b',},
                  '3': {'east','right', 'e', 'r',},
                  '4': {'west', 'left', 'w', 'l'}
                 }
				 
	# Dictionary of acceptance responses and their variants
    keep_playing = {
        'yes': {'y', 'yes', 'yeah', 'yup', 'affirmative'},
        'no': {'n', 'no' , 'nope', 'nah', 'na', 'nope'}
    }
    
	# Constructor
    def __init__(self, rooms, startingRoom):
        """adventureGame constructor. 
    
        Parameters
        ----------
        rooms : Room[]
            Array of the rooms that make up the labyrinth for this specific game. 
        startingRoom : Room()
            The room that the player starts off in for this game.
 
        """
        self.rooms = rooms
        self.current_room = startingRoom
        self.starting_room = startingRoom
    
	# Function to run game
    def play_game(self):
        """Starts the game on the adentureGame that calls playGame(). 
    
        Parameters
        ----------
        self : adventureGame()
            Object that is calling this method.


        """
        
        # print game instructions
        print(self.instructions)
        # game loop
        while True:
            # display current location
            print()
            print('You {}.'.format(self.current_room.name))
            print(self.current_room.description)
            # get player input
            command = input('\nWhich way do you go? \t').strip()
            # assess player movement
            if command.lower() in self.directions['1']:
                if self.current_room.north != None:
                    # go to northern room
                    self.current_room = self.rooms[self.current_room.north]
                else:
                    # invalid movement
                    print('You can\'t go that way.')
            elif command.lower() in self.directions['2']:
                if self.current_room.south != None:
                    # go to southern room
                    self.current_room = self.rooms[self.current_room.south]
                else:
                    # invalid movement
                    print('You can\'t go that way.')
            elif command.lower() in self.directions['3']:
                if self.current_room.east != None:
                    # Go to eastern room
                    self.current_room = self.rooms[self.current_room.east]
                else:
                    # invalid movement
                    print('You can\'t go that way.')
            elif command.lower() in self.directions['4']:
                if self.current_room.west != None:
                    # Go to western room
                    self.current_room = self.rooms[self.current_room.west]
                else:
                    # invalid movement
                    print('You can\'t go that way.')
            # quit game
            elif command.lower() in ('q', 'quit', 'end', 'exit'):
                print('Thanks for playing! See you next time! :)')
                break
            # invalid command
            else:
                print('Sorry, you cannot do that :(' )
            # Check if the room entered kills you
            if self.current_room.kills:
                # Print death dialogue
                print('You {}.'.format(self.current_room.name) )
                print(self.current_room.description)
                print(self.current_room.deathMessage)
                cont = input('\nDo wish to start over? Y/N \t').strip()
                # Restart the game 
                if cont.lower() in self.keep_playing['yes']:
                    self.current_room = self.starting_room
                else:
                    print("Thanks for playing! See you next time! :)")
                    break
            # Check if the room entered is the treasure room
            if self.current_room.treasure:
                # Print treasure dialogue
                print('You {}.'.format(self.current_room.name) )
                print(self.current_room.description)
                print('You have found the treasure! You can\'t wait until you can Tweet about this to all of your followers! #Winning #GameOver')
                cont = input('\nDo wish to start over? Y/N \t').strip()
                # Restart the game 
                if cont.lower() in self.keep_playing['yes']:
                    self.current_room = self.starting_room
                else:
                    print("Thanks for playing! See you next time! :)")
                    break
    