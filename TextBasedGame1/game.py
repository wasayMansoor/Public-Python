#TO DO
#   Change Monster1 To Player                           #Done
#   Implement Experience And Leveling
    #   Gain Of XP If Player Wins                       #Done
    #   Implement Calculation Of XP Depending On        #Done
    #   Implement Points                                #Done
    #   Implement Upgrading With Points                 #Done
    #   Implement level up depending ON XP              #Done

#   Implement Different Move Types
    #   Certain moves are better for certain monsters   #Done
#   Implement Run Away Method                           #Done
#   Add Monster   

import random
#Which Monster Can Be Chosen Depending On Player Level
global maxMonster
maxMonster = 2

#Class for Player
class Player:
    def __init__(self, name, hp, attack1, attack1Power, attack2, attack2Power, attack3, attack3Power, attack4, attack4Power, defense, speed, level=1, xp=0, points=0):
        self.name = name
        self.hp = hp
        self.attack = [attack1, attack2, attack3, attack4]
        self.attackPower = [attack1Power, attack2Power, attack3Power, attack4Power]
        self.defense = defense
        self.speed = speed
        self.level = 1
        self.xp = 0
        self.points = 0



    #Return Methods
    def returnName(self):
        return("Monster's name is " + self.name)

    def returnHealth(self):
        health = str(self.hp)
        return(self.name + " health: " + health)

    def returnAttack(self):
        attack = self.attack
        attackPower = self.attackPower
        for i in range(len(attack)):
            print("Move " + str(i+1) + ": " + str(attack[i]) + ", Power: ", str(attackPower[i]))

    def returnDefense(self):
        defense = str(self.defense)
        return(self.name + " defense: " + defense)

    def returnSpeed(self):
        speed = str(self.speed)
        return(self.name + " speed: " + speed)
    
    def returnLevel(self):
        level = str(self.level)
        return(self.name + " level: " + level)
    
    def returnXp(self):
        xp = str(self.xp)
        return(self.name + " xp: " + xp)

#Class for Monster
class Monster:
    def __init__(self, name, hp, attackName, attackPower, defense1, defense2, defense3, defense4, speed, level, xp, runAwayChance):
        self.name = name
        self.hp = hp + (0.8* level)
        self.attack = attackName
        self.attackPower = attackPower + (0.5 * level)
        self.defense = [defense1, defense2, defense3, defense4]
        self.speed = speed
        self.level = level
        self.xp = xp * level
        self.runAwayChance = runAwayChance


    #Return Methods
    def returnName(self):
        return("Monster's name is " + self.name)

    def returnHealth(self):
        health = str(self.hp)
        return(self.name + " health: " + health)

    def returnAttackName(self):
        return(self.attacNamek)

    def returnAttackPower(self):
        return(self.attackPower)

    def returnDefense(self):
        defense = str(self.defense)
        return(self.name + " defense: " + defense)

    def returnSpeed(self):
        speed = str(self.speed)
        return(self.name + " speed: " + speed)

    def returnLevel(self):
        level = str(self.level)
        return(self.name + " level: " + level)

    def returnXp(self):
        xp = str(self.xp)
        return(self.name + " xp: " + xp)

#Battle Function
def battle(Player, Monster):
    #Intilizing Healths Taken From  Objects
    playerHP = Player.hp
    monsterHP = Monster.hp
    #Battle Will Repeat Until A Monster Dies
    while (playerHP > 0) and (monsterHP > 0):
        print("\n-------------------------------------------------------------- \n")
        #Rounding Healths So We Dont Get Long Decimal Due to Fraction Defenses On Monsters
        playerHP = round(playerHP,1)
        monsterHP = round(monsterHP,1)

        #Printing Out Info
        print(Player.name + "'s HP: " + str(playerHP))
        print("Monster Name: " + Monster.name + " | Monster HP: " + str(monsterHP) + " | Monster Level: " + str(Monster.level))
        print()
        
        #Player Move And Enemy Move Initialized
        moveChosen = 0

        #Will Print Out Attack Options For Player
        Player.returnAttack()
        print("Move 5: Run")

        #Repeats Until A Valid Move Is Chosen
        while (moveChosen < 1) or (moveChosen > 5):
            moveChosen = int(input("\nChoose A Move: "))
        moveChosen = moveChosen-1

        #Empty Line For Cleaner Look
        print()

        if moveChosen !=4:
            #If Statement Determining Who Goes First
            if (Player.speed >= Monster.speed):
            
                #DMG Calculated
                dmg = Player.attackPower[moveChosen] - (Player.attackPower[moveChosen] * Monster.defense[moveChosen])
                dmg = round(dmg,1)

                #Will Only Do Dmg if its above 0
                if dmg > 0:
                    monsterHP = monsterHP - dmg
                    print(Player.name + " dealt " + str(dmg) + " points of damage to " + Monster.name)
                else:
                    print(Player.name + " dealt 0 points of dmg to " + Monster.name)

                #Will Check If Defending Monster Is Dead Or Not
                if monsterHP <= 0:
                    break
                print()

                dmg = Monster.attackPower - Player.defense
                dmg = round(dmg,1)
                if dmg > 0:
                    playerHP = playerHP - dmg
                    print(Monster.name + " dealt " + str(dmg) + " points of damage to " + Player.name)
                else:
                    print(Monster.name + " dealt 0 points of dmg to " + Player.name)

            else:
                dmg = Monster.attackPower - Player.defense
                dmg = round(dmg,1)
                if dmg > 0:
                    playerHP = playerHP - dmg
                    print(Monster.name + " dealt " + str(dmg) + " points of damage to " + Player.name)
                else:
                    print(Monster.name + " dealt 0 points of dmg to " + Player.name)

                if playerHP <= 0:
                    break
                print()
            
                dmg = Player.attackPower[moveChosen] - (Player.attackPower[moveChosen] * Monster.defense[moveChosen])
                dmg = round(dmg,1)
                if dmg > 0:
                    monsterHP = monsterHP - dmg
                    print(Player.name + " dealt " + str(dmg) + " points of damage to " + Monster.name)
                else:
                    print(Player.name + " dealt 0 points of dmg to " + Monster.name)
        #If Player Chooses To Run
        else:
            #Random Chance Of Escaping
            chance = random.randint(1,10)

            #Player's Chance Of Running Away Needs To Be Higher Than The Set Value Of The Monster
            if (chance > Monster.runAwayChance):
                print("You Ran Away")
                Menu()

            #IF Player Does Not Get Away Than Monster Will Do Dmg
            else:
                dmg = Monster.attackPower - Player.defense
                dmg = round(dmg,1)
                if dmg > 0:
                    playerHP = playerHP - dmg
                    print(Monster.name + " dealt " + str(dmg) + " points of damage to " + Player.name)
                else:
                    print(Monster.name + " dealt 0 points of dmg to " + Player.name)
    
    print()
    #XP Leveling Depending If Player Won Or Not And Output Msg
    if (playerHP > 0):
        print ("You Won The Battle!")
        Player.xp = Player.xp + Monster.xp
        LevelUP(Player)

    else:
        print ("You Lost The Battle!")
        Menu()

#Function For Leveling UP
def LevelUP(Player):
    global monsters
    global maxMonster

    #Player Levels Up When He Gets 50 xp
    if Player.xp == 50:
        Player.level = Player.level + 1
        Player.xp = 0
        #2 Upgrade Points Added Every Level
        Player.points = Player.points + 2

    #Every 5 Levels, Higher Level Monsters Are Unlocked, This Value Can Be Changed For Harder Difficulty
    if (Player.level%5 == 0) and (maxMonster < len(monsters)):
        maxMonster += 1
    
    Menu()

#Function For Upgrading
def Upgrade(Player):
    print("\n-------------------------------------------------------------- \n")

    #Outputs Current Upgrade Points
    print(Player.points)

    #Will Continue If Player Has Points
    if Player.points > 0:
        choose = 0

        #Player Chooses What To Upgrade
        print("What Would You Like To Upgrade: ")
        choose = int(input("1. Moves \n2. HP \n3. Defense \n4. Speed \n>"))

        #If Player Chooses Moves Then Game Will Ask What Move
        if choose == 1:
            choose = 0

            Player.returnAttack()
            choose = int(input("1. Move1 \n2. Move2 \n3. Move3 \n4. Move4"))

            if (choose > 0) and (choose <5):
                choose = choose - 1
                Player.attackPower[choose] += 5
            else:
                print("Not Valid")

        #HP, Speed And Defense Upgrading
        elif choose == 2:
            Player.hp += 5
        elif choose == 3:
            Player.defense += 5
        elif choose == 4:
            Player.speed += 5
        else:
            print("Not Valid")
    else:
        print("Not Enough Points To Upgrade Skills!")
    Menu()

#Main Menu
def Menu():

    #All Monsters Are Intialized
    global maxMonster
    global monsters
    spider = Monster("Spider", 20, "a", 10, 0.1, 0.8, 1, 1, 30, random.randint(1, 15), 10, 3)
    lizard = Monster("Lizard", 5, "a", 5, 0.1, 0.8, 1, 1, 15, random.randint(1, 10), 5, 2)
    dinosaur = Monster("dinosaur", 5, "a", 5, 0.1, 0.8, 1, 1, 15, random.randint(1, 10), 5, 3)
    monsters = [spider, lizard, dinosaur]
    
    print("\n-------------------------------------------------------------- \n")
    Choose = 0

    #Player Chooses What To DO
    Choose = int(input("1. Battle \n2. Upgrade \n3. Player Info \n4. Exit\n>"))

    #Game Chooses Random Monster Depending On Player Level
    if Choose == 1:
        monsterNo = random.randrange(0, maxMonster)
        currentMonster = monsters[monsterNo]
        battle(player, currentMonster)

    #Game Starts Upgrade Function
    elif Choose == 2:
        Upgrade(player)

    #Game Outputs Player Info
    elif Choose == 3:
        print()
        print(player.returnHealth())
        player.returnAttack()
        print(player.returnDefense())
        print(player.returnSpeed())
        print(player.returnXp())
        print(player.returnLevel())
        Menu()

    #Game Exits
    elif Choose == 4:
        exit()

    #If Valid Choice Not Picked Then Game Restarts Main Menu
    else:
        print("Not Valid!")
        Menu()
        

Name = str(input("Player's Name: "))     
player = Player(Name, 20, "Punch", 10, "Guns", 20, "Staff", 30, "Sword", 40, 0, 25)



Menu()

#print(Player.returnName())
#print(Player.returnHealth())
#Player.returnAttack()
#print(Player.returnDefense())
#print(Player.returnSpeed())
#print(Player.returnXp())
#print(Player.returnLevel())
