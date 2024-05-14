import inventory
class Player:
    def __init__(self, name: str, maxHealth: int, health: int, dmg: int, defense: int, isDead: bool, inv: inventory.Inventory):
        self.name = name
        self.maxHealth = maxHealth
        self.health = health
        self.dmg = dmg
        self.defense = defense
        self.isDead = isDead # would this condition even been needed?
        self.inv = inv
        # add error handling later

# add exceptions later
    
    
    
    
