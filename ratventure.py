from random import randint 

# +------------------------
# | Text for various menus 
# +------------------------
main_text = ["New Game",\
             "Resume Game",\
             "View Leaderboard",\
             "Exit Game"]

town_text = ["View Character",\
             "View Map",\
             "Move",\
             "Rest",\
             "Save Game",\
             "Exit Game"]

open_text = ["View Character",\
             "View Map",\
             "Move",\
             "Sense Orb",\
             "Exit Game"]

fight_text = ["Attack",\
              "Run"]

world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]


print("Welcome to Ratventure!")
print("----------------------")

# Code your main program here
''' Edward Neo S10204829 P01
Comments
Basic Requirements
Advanced Requirements
    Program Validation
    View Top 5 Scores 
    Randomise location of Orb Of Power
    Randomise location of Town
... '''
import sys
import random

def new_game(): #Occurs when user starts a new game
    print("Day "+str(stats.get("Day"))+": You are in a town")
    townoptions() #Always start in town
    town_choice = input("Enter choice: ")
    while val_town(town_choice) == False:
        print("Invalid input!")
        town_choice = input("Enter choice: ")
        val_town(town_choice)
    town(town_choice)
    while town_choice == "1" or town_choice == "2":
        townoptions()
        town_choice = input("Enter choice: ")
        while val_town(town_choice) == False:
            print("Invalid input!")
            town_choice = input("Enter choice: ")
            val_town(town_choice)
        town(town_choice)
    if town_choice == "3":
        combat()
        combat_choice = input("Enter choice: ")
        while val_combat(combat_choice) == False:
            print("Invalid input!")
            combat_choice = input("Enter choice: ")
            val_combat(combat_choice)
        if combat_choice == "1":
            attack()
        elif combat_choice == "2":
            run()
def remove_stats(stats):
    file = open("C:\\Users\\etnrx\\Documents\\Np Year 1\\PRG assignments\\ASG\\stats.txt","w")
    for item in stats:
        file.write(item+","+str(stats[item])+"\n")
        
def res_game(): #When user chooses to resume game
    key = []
    value = []
    load_stats = {}
    file = open("C:\\Users\\etnrx\\Documents\\Np Year 1\\PRG assignments\\ASG\\stats.txt")
    file = file.readlines()
    for item in file:
        row = item.split(",")
        key += [row[0],]
        value += [row[1].strip("\n"),]
    for name in range(len(key)):
        if value[name].isdigit() == False:
            load_stats[key[name]] = value[name]#Gets the saved stats into the dicionary load_stats
        elif value[name].isdigit() == True:
            load_stats[key[name]] = int(value[name])  
    stats.update(load_stats) #Updates the hero's stats dictionary
    print("Day "+str(stats.get("Day"))+": You are in a town")
    townoptions()
    town_choice = input("Enter choice: ")
    town(town_choice)
    while town_choice == "1" or town_choice == "2":#Day does not change
        townoptions()
        town_choice = input("Enter choice: ")
        town(town_choice)
    if town_choice == "3":
        combat()
        combat_choice = input("Enter choice: ")
        if combat_choice == "1":
            attack()
        elif combat_choice == "2":
            run()

def load_towns(): #Loads the town location when the game is resumed 
    x_coordinates_town = []
    y_coordinates_town = []
    file = open("C:\\Users\\etnrx\\Documents\\Np Year 1\\PRG assignments\\ASG\\Town_coordinates.txt")
    opened_file = file.readlines()
    for item in opened_file:
        coordinates = item.split(",")
        x_coordinates_town += [coordinates[0],]
        y_coordinates_town += [coordinates[1].strip("\n"),]
    for value in range(len(x_coordinates_town)):
        world_map[int(y_coordinates_town[value])][int(x_coordinates_town[value])] = "T"
        
def val_save_file(): #Check to see if there is a saved file
    key = []
    value = []
    load_stats = {}
    file = open("C:\\Users\\etnrx\\Documents\\Np Year 1\\PRG assignments\\ASG\\stats.txt")
    file = file.readlines()
    for item in file:
        row = item.split(",")
        key += [row[0],]
        value += [row[1].strip("\n"),]
    for name in range(len(key)):
        if value[name].isdigit() == False:
            load_stats[key[name]] = value[name]#Gets the saved stats into the dicionary load_stats
        elif value[name].isdigit() == True:
            load_stats[key[name]] = int(value[name])
    if load_stats == stats: #If saved stats and stats are the same, no saved file
        return True
    if load_stats != stats: #If saved stats different, there is a saved file
        return False 
        

#Program Validation    
def val_move(hero_move): #Validating the input of moving
    x_position = int(stats.get("X"))
    y_position = int(stats.get("Y"))
    if hero_move.isdigit() == True:# if input is a number 
        return False
    if len(hero_move) >1: # if length of input larger than 1
        return False
    if hero_move == "W": 
        y_position -= 1
        if y_position >= 0:
            return True
        else:# Cannot move past the border
            return False
    elif hero_move == "A":
        x_position -=1
        if x_position >=0:
            return True
        else:
            return False
    elif hero_move == "S":
        y_position += 1
        if y_position > 7:
            return False
        else:
            return True
    elif hero_move == "D":
        x_position += 1
        if x_position > 7:
            return False
        else:
            return True
    else:
        return False
def val_combat(combat_choice): #Validates combat choice
    if combat_choice == "1" or combat_choice == "2":
        return True
    else:
        return False
def val_town(town_choice): #Validates town choice 
    if town_choice.isdigit() == False: #if input is not an integer
        return False
    if int(town_choice) < 1 or int(town_choice) > 6: # if input is less than 1 or more than 6
        return False
    if town_choice == " ": # if input is nothing
        return False
    if len(town_choice) > 1: # if length of input more than 1
        return False
    else:
        return True
def val_open(outdoor_choice): #Validates outside choice 
    if outdoor_choice.isdigit() == False: #if input is not an integer
        return False
    if outdoor_choice == " ": #if input is nothing
        return False
    if int(outdoor_choice) < 1  or int(outdoor_choice) > 5: # if input is less than 1 or greater than 5
        return False
    if len(outdoor_choice) > 1: # if input length more than 1
        return False
    else:
        return True
def val_orb(location_x,location_y): #Validates orb location 
    if world_map[location_y][location_x] == "T": # cannot spawn in town
        return False
    elif world_map[location_y][location_x] == "K": # cannot spawn in ratking 
        return False
    else:
        return True
    
def move(): #Movement in the map
    day = int(stats.get("Day"))
    x = int(stats.get("X"))#x-coordinate for map
    y = int(stats.get("Y"))#y-coordinate for map
    row = ""
    print()
    worldmap()
    print("W = up; A = left; S = down; D = right")
    hero_move = input("Your move: ")
    hero_move = hero_move.upper()
    while val_move(hero_move) == False:
        print("Invalid Input!")
        hero_move = input("Your move: ")
        hero_move = hero_move.upper()
        val_move(hero_move)
    if hero_move == "W":
        y-=1 # Move upwards
        if world_map[y][x] == " ":
            world_map[y][x] = "H"
        elif world_map[y][x] == "T":
            world_map[y][x] = "H/T"
        elif world_map[y][x] == "K":
            world_map[y][x] = "H/K"
        if world_map[y+1][x] == "H/T":
            world_map[y+1][x] = "T"
        elif world_map[y+1][x] == "H":
            world_map[y+1][x] = " "
        elif world_map[y+1][x] == "H/K":
            world_map[y+1][x] = "K"
    if hero_move == "A":
        x-=1 # Move Left
        if world_map[y][x] == " ":
            world_map[y][x] = "H"
        elif world_map[y][x] == "T":
            world_map[y][x] = "H/T"
        elif world_map[y][x] == "K":
            world_map[y][x] = "H/K"
        if world_map[y][x+1] == "H/T":
            world_map[y][x+1] = "T"
        elif world_map[y][x+1] == "H":
            world_map[y][x+1] = " "
        elif world_map[y][x+1] == "H/K":
            world_map[y][x+1] = "K"
    if hero_move == "S":
        y+=1 # Move Down
        if world_map[y][x] == " ":
            world_map[y][x] = "H"
        elif world_map[y][x] == "T":
            world_map[y][x] = "H/T"
        elif world_map[y][x] == "K":
            world_map[y][x] = "H/K"
        if world_map[y-1][x] == "H/T":
            world_map[y-1][x] = "T"
        elif world_map[y-1][x] == "H":
            world_map[y-1][x] = " "
    if hero_move == "D":
        x+=1 # Move Right
        if world_map[y][x] == " ":
            world_map[y][x] = "H"
        elif world_map[y][x] == "T":
            world_map[y][x] = "H/T"
        elif world_map[y][x] == "K":
            world_map[y][x] = "H/K"
        if world_map[y][x-1] == "H/T":
            world_map[y][x-1] = "T"
        elif world_map[y][x-1] == "H":
            world_map[y][x-1] = " "
    day += 1
    nextday = {"Day":day}
    newx = {"X":x}
    newy = {"Y":y}
    stats.update(nextday)
    stats.update(newx)
    stats.update(newy)
    worldmap()
    
def worldmap(): #Prints the map
    x = int(stats.get("X")) # x-coordinate for map
    y = int(stats.get("Y")) # y-coordinate for map 
    horizontal = ""
    print()
    if world_map[y][x] == "T":
        world_map[y][x] = "H/T"
    if world_map[y][x] == " ":
        world_map[y][x] = "H"
    if world_map[y][x] == "K":
        world_map[y][x] = "H/K"
        
    for col in range(len(world_map)):
        print("+---"*8+"+")
        for row in range(len(world_map)):
            if len(world_map[col][row]) <3:
                horizontal +="| "+str(world_map[col][row])+" "
            else:
                horizontal +="|"+str(world_map[col][row])
        print(horizontal + "|")
        horizontal=""
    print("+---"*8+"+")
    
def townoptions(): #Outputs the options in the town
    for choice in range(len(town_text)):
        print((str(choice+1)+") "+town_text[choice]))
        
def town(town_choice): #Choose town options
    day = int(stats.get("Day"))
    if town_choice == "1":
        print(stats.get("Name")+"\n"
              +"  Damage: " + str(stats.get("MinimumDmg"))+"-"+str(stats.get("MaximumDmg"))+"\n"
              +" Defence: " + str(stats.get("Defence"))+"\n"
              +"      HP: " + str(stats.get("HP")))
        
    elif town_choice == "2":
        worldmap()
    elif town_choice == "3":
        move()
    elif town_choice == "4":
        day += 1
        newday = {"Day":day}
        stats.update(newday)
        print("You are fully healed")
        new_hp = {"HP":20}
        stats.update(new_hp)
        
    elif town_choice == "5":
        file  = open("C:\\Users\\etnrx\\Documents\\Np Year 1\\PRG assignments\\ASG\\stats.txt","w")
        for item in stats:
            file.write(item+","+str(stats[item])+"\n") #Writes the hero stats into text file
        print("Game saved.")
        
    elif town_choice == "6":
        sys.exit()
    
        
def combat(): #Print when outside
    day = int(stats.get("Day"))
    rat_defence = rat_stats.get("Defence")
    rat_HP = rat_stats.get("HP")
    print("Day "+str(day)+": You are out in the open.")
    print("Encouter! - Rat")
    print("Damage: 1-3")
    print("Defence: "+str(rat_defence))
    print("HP: "+str(rat_HP))
    print("1) Attack")
    print("2) Run")
    
def attack(): #When first combat choice is chosen
    rat_defence = rat_stats.get("Defence")
    rat_HP = rat_stats.get("HP")
    HP = int(stats.get("HP"))
    defence = int(stats.get("Defence"))
    while rat_HP > 0 and HP > 0:
        hero_dmg = random.randint(int(stats.get("MinimumDmg")),int(stats.get("MaximumDmg")))
        rat_dmg = random.randint(rat_stats.get("MinimumDmg"),rat_stats.get("MaximumDmg"))
        dmg_done = (rat_dmg - defence)
        if dmg_done < 0:
            dmg_done = 0 # Prevents showing negative number
        HP = HP-(rat_dmg-defence)
        rat_HP = rat_HP - (hero_dmg-rat_defence)
        print("You deal "+str(hero_dmg-rat_defence)+" damage to the Rat")
        if rat_HP <= 0:
            print("The Rat is dead! You are victorious!")
            outdooroptions()
            outdoor_choice = input("Enter choice: ")
            while val_open(outdoor_choice) == False:
                print("Invalid Input!")
                outdoor_choice = input("Enter choice: ")
                val_open(outdoor_choice)
            while outdoor_choice == "1" or outdoor_choice == "2" or outdoor_choice == "4": #Day does not change
                outdoor(outdoor_choice)
                outdooroptions()
                outdoor_choice = input("Enter choice: ")
                while val_open(outdoor_choice) == False:
                    print("Invalid Input!")
                    outdoor_choice = input("Enter choice: ")
                    val_open(outdoor_choice)
            outdoor(outdoor_choice)                    
            break #Exits the while loop
        print("Ouch! The Rat hit you for "+str(dmg_done)+" damage!")
        print("You have "+str(HP)+" HP left.")
        if HP <= 0:
            print("You have died. Game Over!")
            sys.exit()
        print("Damage: 1-3")
        print("Defence: "+str(rat_defence))
        print("HP: "+str(rat_HP))
        print("1) Attack")
        print("2) Run")
        combat_choice = input("Enter choice: ")
        while val_combat(combat_choice) == False:
            print("Invalid Input!")
            combat_choice = input("Enter choice:")
            val_combat(combat_choice)
        HP_remainder = {"HP":HP}
        stats.update(HP_remainder)
        if combat_choice == "2":
            run()
        
def run():#When second combat choice is chosen
    print("You run and hide.")
    outdooroptions()
    outdoor_choice = input("Enter choice: ")
    while val_open(outdoor_choice) == False:
        print("Invalid Input!")
        outdoor_choice = input("Enter choice: ")
        val_open(outdoor_choice)
    outdoor(outdoor_choice)
    if outdoor_choice == "1" or outdoor_choice == "2" or outdoor_choice == "4":
        combat()#Since user did not move nor quit, have to fight again
        combat_choice = input("Enter choice: ")
        while val_combat(combat_choice) == False:
            print("Invalid Input!")
            combat_choice = input("Enter choice: ")
            val_combat(combat_choice)
        if combat_choice == "1":
            attack()
        elif combat_choice == "2":
            run()
def outdooroptions(): #Displays outside options
    day = stats.get("Day")
    print("Day "+str(day)+": You are in the open")
    for choice in range(len(open_text)):
        print((str(choice+1)+") "+open_text[choice]))
        
def outdoor(outdoor_choice): #Actions taken when user makes an option
    day = stats.get("Day")
    if outdoor_choice == "1":
         print(stats.get("Name")+"\n"
              +"  Damage: " + str(stats.get("MinimumDmg"))+"-"+str(stats.get("MaximumDmg"))+"\n"
              +" Defence: " + str(stats.get("Defence"))+"\n"
              +"      HP: " + str(stats.get("HP")))
         if int(stats.get("Defence")) == 6: #proof of Orb of Power in posession
             print("You are holding the Orb of Power")
    elif outdoor_choice == "2":
        worldmap()
    elif outdoor_choice == "3":
        move()
    elif outdoor_choice == "4":
        if int(stats.get("Defence")) == 1:
            senseorb(location_x, location_y) #Notifies user which direction 
            senseorb_pickup(outdoor_choice)  #When user picks up the orb
        if int(stats.get("Defence")) == 6:
            print("The orb has been found and picked up.")
    elif outdoor_choice == "5":
        sys.exit()

        
def senseorb_found(location_x,location_y): #Checks to see if Hero's location is on Orb of Power
    x_coordinates = int(stats.get("X"))
    y_coordinates = int(stats.get("Y"))
    if location_x == x_coordinates and location_y == y_coordinates:
        return True
    else:
        return False 
def senseorb_pickup(outdoor_choice): #When user picks up the orb
    if outdoor_choice == "4":
        if senseorb_found(location_x, location_y) == True:
            print("You found the orb.")
            print("Your attack increases by 5!")
            print("Your defence increases by 5!")
            min_dmg = int(stats.get("MinimumDmg"))
            max_dmg = int(stats.get("MaximumDmg"))
            defence = int(stats.get("Defence"))
            new_min_dmg = min_dmg + 5
            add_min_dmg = {"MinimumDmg":new_min_dmg}
            stats.update(add_min_dmg)
            new_max_dmg = max_dmg + 5
            add_max_dmg = {"MaximumDmg":new_max_dmg}
            stats.update(add_max_dmg)
            new_defence = defence + 5
            add_defence = {"Defence":new_defence}
            stats.update(add_defence)
    
def senseorb(location_x,location_y): #Notifies users which direction the Orb of Power is
    day = stats.get("Day")
    next_day = day +1
    add_day = {"Day":next_day}
    stats.update(add_day)
    x_coordinates = int(stats.get("X"))
    y_coordinates = int(stats.get("Y"))
    if location_x > x_coordinates and location_y > y_coordinates :
        print("You sense that the orb of Power is to the southeast")
    elif location_x > x_coordinates and location_y < y_coordinates:
        print("You sense that the orb of power is to the northeast")
    elif location_x < x_coordinates and location_y < y_coordinates:
        print("You sense that the orb of power is to the northwest")
    elif location_x < x_coordinates and location_y > y_coordinates:
        print("You sense that the orb of power is to the southwest")
    elif location_x == x_coordinates and location_y > y_coordinates:
        print("You sense that the orb of power is to the south")
    elif location_x == x_coordinates and location_y < y_coordinates:
        print("You sense that the orb of power is to the north")
    elif location_x < x_coordinates and location_y == y_coordinates:
        print("You sense that the orb of power is to the west")
    elif location_x > x_coordinates and location_y == y_coordinates:
        print("You sense that the orb of power is to the east")
        
def ratking_menu(): #Displays the combat menu with Rat King
    print("Encounter! - Rat King")
    print("Damage: 6-10")
    print("Defence: 5")
    print("HP: "+str(ratking_stats.get("HP")))
    for choice in range(len(fight_text)):
        print(str(choice+1)+") "+fight_text[choice])
        
def ratking_attack(): #When user chooses to attack Rat King
    ratking_defence = ratking_stats.get("Defence")
    ratking_HP = ratking_stats.get("HP")
    defence = int(stats.get("Defence"))
    HP = int(stats.get("HP"))
    ratking_mindmg = ratking_stats.get("MinimumDmg")
    ratking_maxdmg = ratking_stats.get("MaximumDmg")
    hero_mindmg = int(stats.get("MinimumDmg"))
    hero_maxdmg = int(stats.get("MaximumDmg"))
    ratking_dmg = random.randint(ratking_mindmg,ratking_maxdmg)
    hero_dmg = random.randint(hero_mindmg,hero_maxdmg)
    if int(stats.get("Defence")) == 1: # No orb of power in posession
        print("You do not have the Orb of Power - the Rat King is immune!")
        print("You deal 0 damage to the Rat king")
        print("Ouch! The Rat King hit you for "+str(ratking_dmg-defence)+" damage!")
        HP = HP-(ratking_dmg - defence)
        if HP <= 0:
            HP = 0
            print("Game Over!")
            sys.exit()
        add_HP = {"HP":HP}
        stats.update(add_HP)
        if HP >0:
            print("You have "+str(HP)+" HP left.")  
            ratking_menu()
            combat_choice = input("Enter choice: ")
            while val_combat(combat_choice) == False:
                print("Invalid Input!")
                combat_choice = input("Enter choice: ")
                val_combat(combat_choice)
            if combat_choice == "1":
                ratking_attack()
            elif combat_choice == "2":
                run()
                ratking_HP = 25
                add_ratking_HP = {"HP":ratking_HP}
                ratking_stats.update(add_ratking_HP)

    elif int(stats.get("Defence")) == 6: # Proof of Orb of Power in posession
        ratking_HP = ratking_HP - (hero_dmg - ratking_defence)
        new_ratking_HP = {"HP":ratking_HP}
        ratking_stats.update(new_ratking_HP)
        HP = HP -(ratking_dmg-defence)
        add_HP = {"HP":HP}
        stats.update(add_HP)
        print("You deal "+str(hero_dmg-ratking_defence)+" damage to the Rat King")
        print("Ouch! The Rat King hit you for "+str(ratking_dmg-defence)+" damage!")
        if ratking_HP <= 0:
            print("The Rat King is dead! You are victorious!")
            print("Congratulations, you have defeated the Rat King!")
            print("The world is saved! You win!")
            add_leaderboard(key,value)
            sys.exit()
            

        elif HP <=0:
            HP = 0
            print("You have "+str(HP)+" HP left.")
            print("You have died. Game Over!")
            sys.exit()
        print("You have "+str(HP)+" HP left.")
        ratking_menu()
        combat_choice = input("Enter choice: ")
        while val_combat(combat_choice) == False:
            print("Invalid Input!")
            combat_choice = input("Enter choice: ")
            val_combat(combat_choice)
        if combat_choice == "1":
                ratking_attack()
        elif combat_choice == "2":
            run()
            ratking_HP = 25
            add_ratking_HP = {"HP":ratking_HP}
            ratking_stats.update(add_ratking_HP)
        print()

def add_leaderboard(key,value): #Overwrites the Leaderboard with the smallest days
    file = open("C:\\Users\\etnrx\\Documents\\Np Year 1\\PRG assignments\\ASG\\Leaderboard.txt","w")
    value += [stats.get("Day"),]
    value.sort()
    for name in range(len(key)):
        file.write(key[name]+","+str(value[name])+"\n")

def town_removal(): #Removes Pre-set towns
    x_coordinates = 0
    y_coordinates = 0
    for y in range(7):
        for x in range(7):
            if world_map[y][x] == "T":
                world_map[y][x] = " "
        world_map[y_coordinates][x_coordinates] = "T" #Ensures the first box is always a town       

def random_town(): #Randomises and validates the new towns position
    ran_town = [random.randint(0,7),random.randint(0,7)]
    towns = []
    probihited = [[0,0],[0,1],[1,0],[1,1],[2,0],[0,2],[7,7],[location_x,location_y]]#Coordinates where the town cannot be in
    for count in range(4):
        while ran_town in probihited:
            ran_town = [random.randint(0,7),random.randint(0,7)]
        if ran_town not in probihited:
            x = ran_town[0]
            y = ran_town[1]
            #list of accepted random coordinates
            towns += [[x,y],]
            #adds to the list of coordinates where towns cannot be added
            probihited += [[x,y],]
            probihited += [[x+1,y],]
            probihited += [[x+2,y],]
            probihited += [[x,y+1],]
            probihited += [[x,y+2],]
            probihited += [[x+1,y+1],]
            probihited += [[x-1,y],]
            probihited += [[x-2,y],]
            probihited += [[x-1,y+1],]
            probihited += [[x,y-1],]
            probihited += [[x,y-2],]
            probihited += [[x+1,y-1],]
            probihited += [[x-1,y-1],]
    town_location(towns)          
    save_town(towns)#Writes the coordinates of the town into text document 
def town_location(towns): #Insert the random and validated coordinates of the town into the world map
    for coordinates in range(len(towns)):
        y_coordinates = towns[coordinates][1]
        x_coordinates = towns[coordinates][0]
        world_map[y_coordinates][x_coordinates] = "T"
def save_town(towns): #Saves the randomised coordinates of the town
    file = open("C:\\Users\\etnrx\\Documents\\Np Year 1\\PRG assignments\\ASG\\Town_coordinates.txt","w")
    for coordinates in towns:
        #Dont need to split as coordinates is [x,y]
        x_coordinate = coordinates[0]
        y_coordinate = coordinates[1]
        file.write(str(x_coordinate)+","+str(y_coordinate)+"\n")


    
#Main Code
#Dictionaries for stats
stats = {"Name":"The Hero", "MinimumDmg":2, "MaximumDmg":4,"Defence":1,"HP":20,"X":0,"Y":0,"Day":1}
ratking_stats = {"MinimumDmg":6,"MaximumDmg":10,"Defence":5,"HP":25}
rat_stats = {"MinimumDmg":1,"MaximumDmg":3,"Defence":1,"HP":10}
#To get leaderboard
file = open("C:\\Users\\etnrx\\Documents\\Np Year 1\\PRG assignments\\ASG\\Leaderboard.txt")
opened_file = file.readlines()
key = []
value = []
for item in opened_file:
    char = item.split(",")
    key += [char[0],] # To get 1st,2nd,3rd
    value += [int(char[1].strip("\n")),]# To get days per attempt
file.close()
#Remove pre set towns
town_removal()
#Used to for random placement of Orb of Power
location_x = random.randint(0,7)
if location_x >= 4:
    location_y = random.randint(0,7)
elif location_x < 4:
    location_y = random.randint(4,7)
if val_orb(location_x, location_y) == False:
    location_x = random.randint(0,7)
    if location_x >= 4:
        location_y = random.randint(0,7)
    elif location_x < 4:
        location_y = random.randint(4,7)
    val_orb(location_x, location_y)
    
#Displaying the main menu text
for text in range(len(main_text)):
    print(str(text+1)+") "+main_text[text])
menu_choice = input("Enter choice: ")
if menu_choice == "1":
    #Removes any saved data of hero
    remove_stats(stats)
    #Randomly adding new ones
    random_town()
    #Prints the town options
    new_game()
    
if menu_choice == "2":
    if val_save_file() == True: #If there is no saved file
        print("No save file found!"+"\n"+"Starting new game!")
        remove_stats(stats)
        random_town()
        new_game()
    elif val_save_file() == False:# If there is a saved file
        load_towns() # Load new towns
        res_game() # Resumes game
while menu_choice == "3":
    for number in range(len(value)):
        if value[number] == 100:#If attempts less than 5, 100 would be displayed for the attempts not done yet
            value[number] = " " #To hide the 100
        print(key[number]+") "+str(value[number]))
    menu_choice = input("Enter choice: ")
    if menu_choice == "1":
        #town_removal()
        remove_stats(stats)
        random_town()
        new_game()
    if menu_choice == "2":
        '''if val_save_file() == True: #If there is no saved file
            print("No save file found!"+"\n"+"Starting new game!")
            remove_stats(stats)
            random_town()
            new_game()
        elif val_save_file() == False:# If there is a saved file
            load_towns() # Load new towns'''
        res_game() # Resumes game
    if menu_choice == "4":
        sys.exit()
if menu_choice == "4":
    sys.exit()
    
while int(stats.get("HP")) > 0:
    y_coordinates = int(stats.get("Y"))
    x_coordinates = int(stats.get("X"))
    
    if world_map[y_coordinates][x_coordinates] == "H/T": # When hero enters the town 
        print("Day "+str(stats.get("Day"))+": You are in a town")
        townoptions()
        town_choice = input("Enter choice: ")
        if val_town(town_choice) == False:
            print("Invalid Input!")
            town_choice = input("Enter choice: ")
            val_town(town_choice)
        town(town_choice)
        while town_choice == "1" or town_choice == "2":#Day has not pass
            townoptions()
            town_choice = input("Enter choice: ")
            town(town_choice)
        if town_choice == "3":
            if world_map[y_coordinates][x_coordinates] == "H/K": # In the event that town spawn beside rat king
                print("Day "+str(stats.get("Day")+": You see the Rat King!")
                ratking_menu()
                combat_choice = input("Enter choice: ")
                while val_combat(combat_choice) == False:
                    print("Invalid Input!")
                    combat_choice = input("Enter choice: ")
                    val_combat(combat_choice)
                if combat_choice == "1":
                    ratking_attack()
                elif combat_choice == "2":
                    run()
            elif world_map[y_coordinates][x_coordinates] == "H":
                combat()
                combat_choice = input("Enter choice: ") 
                while val_combat(combat_choice) == False:
                    print("Invalid Input!")
                    combat_choice = input("Enter choice: ")
                    val_combat(combat_choice)
                if combat_choice == "1":
                    attack()
                elif combat_choice == "2":
                    run()
                    combat()
                
    if world_map[y_coordinates][x_coordinates] == "H": # When hero enters a blank space
        combat()
        combat_choice = input("Enter choice: ")
        while val_combat(combat_choice) == False:
            print("Invalid Input!")
            combat_choice = input("Enter choice: ")
            val_combat(combat_choice)
        if combat_choice == "1":
            attack()
        elif combat_choice == "2":
            run()
        
    if world_map[y_coordinates][x_coordinates] == "H/K":# When hero encouters ratking 
        day = stats.get("Day")
        print("Day "+str(day)+": You see the Rat King!")
        ratking_menu()
        combat_choice = input("Enter choice: ")
        while val_combat(combat_choice) == False:
            print("Invalid Input!")
            combat_choice = input("Enter choice: ")
            val_combat(combat_choice)
        if combat_choice == "1":
            ratking_attack()
        elif combat_choice == "2":
            run()

