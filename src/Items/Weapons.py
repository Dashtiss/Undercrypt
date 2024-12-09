from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.Items.Item import Item

class WeaponType(Enum):
    MELEE = 0
    RANGED = 1
    MAGIC = 2
    NONE = 3


class Weapon:
    def __init__(
        self,
        name: str,
        damage: int,
        Type: WeaponType = WeaponType.NONE,
    ):
        self.name = name
        self.damage = damage
        self.type = Type
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other: Weapon):
        return self.name == other.name
    
    