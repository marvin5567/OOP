entityTypes = ['NPC', 'ENEMY', 'ANIMAL']
hostilityTypes = ['Peaceful', 'Neutral', 'Hostile', 'Aggressive']
class Entity:
    def __init__(self, name: str, maxHealth: int, health: int, defense: int, entityType: str, hostility: str, drops: list = []):
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.defense = defense
        self.entityType = entityType
        self.hostility = hostility
        self.drops = drops # 
        
        if not isinstance(name, str):  
            raise TypeError("Entity Name must be a string value")
        if not isinstance(health, int):
            raise TypeError("Entity Health must be an integer value")
        if not isinstance(defense, int):
            raise TypeError("Entity Defense must be an integer value")
        if not isinstance(entityType, str):
            raise TypeError("Entity Type must be a string value")
        if not isinstance(hostility, str):
            raise TypeError("Entity Hostility must be a string value")
        self.checkEntityType()

    def checkEntityType(self):
        if self.entityType.upper() not in entityTypes: # is it valid?
            raise invalidEntityType # if not, raise exception

    def checkEntityHostility(self):
        if self.hostility.upper() not in hostilityTypes:
            raise invalidHostilityType

    def entityInfo(self): # info function
        return f"Entity Info\n-----------\nName: {self.name}\nHealth: {self.health}\nDefense: {self.defense}\nEntity Type: {self.entityType}\nHostility: {self.hostility}\nDrops: {self.drops}"
    
    def healthDisplay(self): # for the sake of simplicity and not having to write it out every time
        return "{n} HP: {hp}/{mhp}"

    def healthChange(self, incomingHealthChange):
        if self.maxHealth <= self.health + incomingHealthChange:
            self.health == self.maxHealth
            return self.healthDisplay()

        else:
            currentHealth = self.health
            self.health += incomingHealthChange
            if currentHealth > self.health:
                print(f"Gained {incomingHealthChange} HP!")
                return self.healthDisplay()
            
            if currentHealth < self.health:
                print(f"Lost {abs(incomingHealthChange)} HP!")
                return self.healthDisplay()

# could hostilies be classes?

# inherited classes
class NPC(Entity):
    def __init__(self, maxHealth: int, name: str, health: int, defense: int, entityType: str, hostility: str, drops: list = []):
        super().__init__(name, maxHealth, health, defense, entityType, hostility, drops)

    def entityInfo(self):
        return f"{super().entityInfo()}\nidk man i'll add more attributes later"
    
    def healthDisplay(self):
        return super().healthDisplay().format(n=self.name, hp=self.health, mhp=self.maxHealth)

    def healthChange(self, incomingHealthChange):
        return super().healthChange(incomingHealthChange).format(name=self.name)
    
class Enemy(Entity):
    def __init__(self, maxHealth: int, name: str, health: int, defense: int, entityType: str, hostility: str, drops: list = []):
        super().__init__(name, maxHealth, health, defense, entityType, hostility, drops)
    
    def entityInfo(self):
        return f"{super().entityInfo()}"

    def healthDisplay(self):
        return super().healthDisplay().format(n=self.name, hp=self.health, mhp=self.maxHealth)

    def healthChange(self, incomingHealthChange):
        return super().healthChange(incomingHealthChange)

class Animal(Entity):
    def __init__(self, name: str, maxHealth: int, health: int, defense: int, entityType: str, hostility: str, drops: list = []):
        super().__init__(name, maxHealth, health, defense, entityType, hostility, drops)
    
    def entityInfo(self):
        return f"{super().entityInfo()}"
    
    def healthDisplay(self):
        return super().healthDisplay().format(n=self.name, hp=self.health, mhp=self.maxHealth)

    def healthChange(self, incomingHealthChange):
        return super().healthChange(incomingHealthChange).format(name=self.name)

# custom exceptions
class invalidEntityType(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid entity type, you sure you have the correct entity type?"

class invalidHostilityType(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid entity hostility. Please check your spelling!! Because i cant spell hositlity for the life of me!!!"
