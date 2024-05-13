itemTypes = ['FOOD', 'WEAPON', 'TOOl', 'ARMOUR']
class Item:
    def __init__(self, id: int, name: str, desc: str, itemType: str):
        self.id = id
        self.name = name
        self.desc = desc
        self.itemType = itemType
        self.isItemTypeValid()
            

    def isItemTypeValid(self):
        if self.itemType.upper() not in itemTypes:
            raise invalidItemType
        
        else:
            exec(f'self.create{self.itemType.upper()}()')

    def createFOOD(self):
        pass
    def createWEAPON(self):
        pass
    def createARMOUR(self):
        pass
    def createTOOL(self):
        pass
class invalidItemType(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid item type, you sure you have the correct object type?"

    