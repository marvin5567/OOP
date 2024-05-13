class Item:
    def __init__(self, id: int, name: str, desc: str, itemType: str):
        self.id = id
        self.name = name
        self.desc = desc
        self.itemType = itemType
        print(itemType.upper())
        self.isItemTypeValid()
            

    def isItemTypeValid(self):
        if self.itemType.upper() != ('FOOD' or 'WEAPON' or 'TOOl' or 'ARMOUR'):
            raise invalidItemType
    
class invalidItemType(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid item type, you sure you have the correct object type?"

    