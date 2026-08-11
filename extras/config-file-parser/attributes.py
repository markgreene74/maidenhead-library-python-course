from enum import StrEnum


class Colour(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
    MAGENTA = "magenta"
    WHITE = "white"


class CharacterClass(StrEnum):
    WARRIOR = "warrior"
    WIZARD = "wizard"
    ROGUE = "rogue"
    ARCHER = "archer"
    PALADIN = "paladin"


class Weapon(StrEnum):
    SWORD = "sword"
    LONG_SWORD = "long sword"
    SHORT_SWORD = "short sword"
    LONG_BOW = "long bow"
    SHORT_BOW = "short bow"
    AXE = "axe"
    MACE = "mace"
    STAFF = "staff"


class Defence(StrEnum):
    LIGHT_WOODEN_SHIELD = "light wooden shield"
    HEAVY_STEEL_SHIELD = "heavy steel shield"
    SHIELD_SPELL = "shield spell"
    NO_DEFENCE = "no defence"


class Armour(StrEnum):
    METAL = "metal"
    LEATHER = "leather"
    NO_ARMOUR = "no armour"
