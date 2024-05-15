import inventory
class Player:
    def __init__(self, name: str, maxHealth:int, health: int, maxHunger: int, hunger: int, dmg: int, defense: int, isDead: bool):
        self.name = name
        self.maxHealth = maxHealth
        self.health = health
        self.dmg = dmg
        self.defense = defense
        self.maxHealth = maxHealth
        self.isDead = isDead
        self.maxHunger = maxHunger
        self.hunger = hunger
        
    def healthCheck(self):
        if self.health <= 0:
            self.isDead == True
            print("You died!!!")
            return self.isDead

    def healthChange(self, incomingHealthChange):
        if self.maxHealth <= self.health + incomingHealthChange:
            self.health == self.maxHealth
            print(f"HP: {self.health}/{self.maxHealth}")
        else:
            self.health += incomingHealthChange
            print(f"HP: {self.health}/{self.maxHealth}")
    
        self.healthCheck()