itemTypes = ['FOOD', 'WEAPON', 'TOOl', 'ARMOUR']
class Item:
    def __init__(self, id: int, name: str, desc: str, itemType: str):
        self.id = id
        self.name = name
        self.desc = desc
        self.itemType = itemType

        # error handling!!
        if not isinstance(id, int):
            raise TypeError("Item ID must be an integer value")

        if not isinstance(name, str):
            raise TypeError("Item Name must be a string value")
        
        if not isinstance(desc, str):
            raise TypeError("Item Description must be a string value")
        
        if not isinstance(itemType, str):
            raise TypeError("Item Type must be a string value")
        
        self.checkItemType()

    def checkItemType(self):
        if self.itemType.upper() not in itemTypes: # is it valid?
            raise invalidItemType # if not, raise exception

    def checkItemInfo(self):
        return f"ID: {self.id}\nName: {self.name}\nDescription: {self.desc}\nItem Type: {self.itemType.upper()}"

class FOOD(Item):
    def __init__(self, id: int, name: str, desc: str, itemType: str, saturation: int, healthGain: int = 0):
        super().__init__(id, name, desc, itemType)
        self.saturation = saturation
        self.healthGain = healthGain
        
        # error handling!!
        if not isinstance(saturation, int):
            raise TypeError("Food Saturation must be an integer value")
        
        if not isinstance(healthGain, int):
            raise TypeError("Food Health Gain must be an integer value")
    
    def checkItemInfo(self):
        itemInfo = super().checkItemInfo()
        return f"{itemInfo}\nSaturation: {self.saturation}\nHealth Gain: {self.healthGain}"

class WEAPON(Item):
    def __init__(self, id: int, name: str, desc: str, itemType: str, attackDMG: int, attackSpeed: int):
        super().__init__(id, name, desc, itemType)
        self.attackDMG = attackDMG
        self.attackSpeed = attackSpeed

    def checkItemInfo(self):
        itemInfo = super().checkItemInfo()
        return f"{itemInfo}\nAttack Damage: {self.attackDMG}\nAttack Speed: {self.attackSpeed}"

class ARMOUR(Item):
    def __init__(self, id: int, name: str, desc: str, itemType: str, defense: int):
        super().__init__(id, name, desc, itemType)
        self.defense = defense
    
    def checkItemInfo(self):
        itemInfo = super().checkItemInfo()
        return f"{itemInfo}\nDefense: {self.defense}"

# custom exceptions
class invalidItemType(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid item type, you sure you have the correct object type?"

    