import pytest
from adventureGame import room as r
from adventureGame import adventureGame as g
from adventureGame import testGame as tg

def test_rooms():
    """Labyrinth room object testing function. 

    Returns
    -------
    True or False depending upon the assertions

    """
    
    # check that the cnstructor is callable
    assert callable(r.Room)
    
    # Create 2 test rooms to test the default room as well as a room with overriden defults 
    room1 = r.Room( 'TestTest', 'Description', 'North', 'South', 'East', 'West' )
    room2 = r.Room( 'Test2', 'D', 'N', 'S', 'E', 'W', kills=True, treasure=True, deathMessage='You died' )
    
    # Test default constructor
    assert room1.name == 'TestTest'
    assert room1.description == 'Description'
    assert room1.north == 'North'
    assert room1.south == 'South'
    assert room1.east == 'East'
    assert room1.west == 'West'
    assert room1.kills == False
    assert room1.treasure == False
    
    # Test constructor that has overriden the defaults
    assert room2.kills == True
    assert room2.treasure == True
    assert room2.deathMessage == 'You died'

def test_game():
    """Adventure game object testing function. 

    Returns
    -------
    True or False depending upon the assertions

    """
    
    # check that all of the functions are callable
    assert callable(g.AdventureGame)
    
    # Load up the rooms for the test game
    testGame = g.AdventureGame(tg.testRooms, tg.starting_room)
    
    # Test that the constructor properly loads the rooms
    assert testGame.rooms == tg.testRooms
    assert testGame.starting_room == tg.starting_room
    assert testGame.current_room == tg.starting_room
    
# run the test functions
test_rooms()
test_game()