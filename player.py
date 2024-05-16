import inventory
class Player:
    def __init__(self, name: str, maxHealth:int, health: int, maxHunger: int, hunger: int, dmg: int, defense: int, isDead: bool):
        self.name = name
        self.maxHealth = maxHealth
        self.health = health
        self.dmg = dmg
        self.defense = defense
        self.maxHealth = maxHealth
        self.isDead = isDead # probably will be depricated, doesnt have much use in my head since we calculating health
        self.maxHunger = maxHunger
        self.hunger = hunger
        
    def healthDisplay(self): # for the sake of simplicity and not having to write it out every time
        return f"HP: {self.health}/{self.maxHealth}"

    def healthChange(self, incomingHealthChange):
        if self.maxHealth <= self.health + incomingHealthChange:
            self.health == self.maxHealth
            return self.healthDisplay()

        else:
            currentHealth = self.health
            self.health += incomingHealthChange
            if currentHealth < self.health:
                print(f"Gained {incomingHealthChange} HP!")
                return self.healthDisplay()
            
            if currentHealth > self.health:
                print(f"Lost {abs(incomingHealthChange)} HP!")
                return self.healthDisplay()