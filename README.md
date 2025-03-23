# Python Simple Game Ratventure
Using Python Programming Language, create a simple computer role-playing game called Ratventure.

# Scope
You are The Hero. The world is being invaded by the Rat King and his endless rat minions. The only way to defeat the Rat King is to find the Orb of Power, and then destroy the Rat King in combat. Since you have the ability to sense the Orb of Power, only you can save the world.

In this computer role-playing game, you will travel around a grid map searching for the Orb of Power and fighting rat minions. On the map are various towns where you can rest and save your game. Once you find the Orb of Power, destroy the Rat King to win the game.   

# Requirements 
1) Display the main menu with options
    1) Start a New game - Default town locations are found in "Town_coordinates.txt" and default player statistics are {"Name": The Hero, "Damage": 2-4, "Defence": 1, "HP": 20}
    2) Resume Game
    3) View Leaderboard - Views the Top 5 scores 
    4) Exit game
2) Display Town menu with options - When moves to a Town square
    1) View Character Stastistics - updated in "stats.txt"
    2) View Map - if hero is in town or at the Rat King Castle, its H/T or H/K
    3) Move - WASD to move one space, adds a day
    4) Rest - Reset's players HP to 20, adds a day
    5) Save - Save's current state of the game
    6) Exit - Quit the game
3) Combat Menu - When hero moves to a blank square
    1) Attack - dealing random damage based on his stat; wild rat also attacks; until either hp reaches 0
    2) Run - Run from the combat and goes to outdoor menu
4) Outdoor Menu - When a player defeats a rat or runs from combat
    1) View Character Statistics
    2) View Map
    3) Move
    4) Sense Orb - Provides a direction of the Orb of Power (North, Northeast etc) unless player is on the square of the orb of power, then stats + 5, adds a day
    5) Exit Game
5) Rat King - Combat menu is displayed; if orb of power is not present, no damage is done
