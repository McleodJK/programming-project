import random

locations = []
locTypes = ["Desert","Forest","Beach"]
enemyType = ["Orc","Elf","Fairy"]

class Location:
    def __init__(self, locType, numEnemies, timeOfDay):
        self.locType = locType
        self.numEnemies = numEnemies
        self.timeOfDay = timeOfDay
        self.enemies = []
        self.visited = False
        
        for i in range(numEnemies):
            self.enemies.append(Enemy(random.choice(enemyType),random.randint(10,20),"Axe"))
           
    def createEnemies(self):
        pass
               
class Enemy:
    def __init__(self, enemyType, enemyHP, weapon):
        self.enemyType = enemyType
        self.enemyHP = enemyHP
        self.weapon = weapon
        self.alive = True
        
   
for i in range(10):
    locations.append(Location(random.choice(locTypes),random.randint(1,5),"Noon"))

"""
counter = 0
while counter < len(locations):    
    print(self.locType)
"""

for location in locations:
    print("*****************"+location.locType +" "+str(location.numEnemies)+"***************")
    for enemy in location.enemies:
        print(enemy.enemyType + " " +str(enemy.enemyHP))
    
    