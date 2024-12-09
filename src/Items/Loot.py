from . import Weapons
import random

# loop table
class LootTable:
    def __init__(self, table: list[Weapons.Weapon]):
        self.table = table
        
    