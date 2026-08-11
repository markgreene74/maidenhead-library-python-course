from enum import StrEnum
from pathlib import Path
from sys import exit

from attributes import Armour, CharacterClass, Colour, Defence, Weapon


def read_config_file(filename: str) -> list[str]:
    """Read a config file and return the contents as a list
    of lines.

    If the file does not exist, raise a RuntimeError."""
    path = Path(filename)

    if not path.exists():
        exit(f"Config file {filename} does not exist")

    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def assign_colour(colour: str) -> StrEnum | None:
    try:
        return Colour(colour)
    except ValueError:
        print(f"Invalid colour value: {colour}")
        return None


def assign_class(character_class: str) -> StrEnum | None:
    try:
        return CharacterClass(character_class)
    except ValueError:
        print(f"Invalid class value: {character_class}")
        return None


def assign_weapon(weapon: str) -> StrEnum | None:
    try:
        return Weapon(weapon)
    except ValueError:
        print(f"Invalid weapon value: {weapon}")
        return None


def assign_defence(defence: str) -> StrEnum | None:
    try:
        return Defence(defence)
    except ValueError:
        print(f"Invalid defence value: {defence}")
        return None


def assign_armour(armour: str) -> StrEnum | None:
    try:
        return Armour(armour)
    except ValueError:
        print(f"Invalid armour value: {armour}")
        return None


def parse_config(content: list[str]) -> dict[str, str | StrEnum | None]:
    """Parse the content of a config file.

    Return a dictionary containing the configuration."""
    result: dict[str, str | StrEnum | None] = {}

    for line in content:
        if line.startswith("#"):
            # it's a comment, skip to the next line
            continue

        # split the line in its components:
        # label :(colon) value
        line_split = line.split(":")
        if len(line_split) != 2:
            print(f"Invalid line format: {line}")
            continue

        label, value = line_split

        # sanitise the label and value
        label = label.strip().lower()
        value = value.strip().lower()

        match label:
            case "colour" | "color":
                result["colour"] = assign_colour(value)
            case "class":
                result["class"] = assign_class(value)
            case "name":
                result["name"] = value
            case "weapon":
                result["weapon"] = assign_weapon(value)
            case "defence" | "defense":
                result["defence"] = assign_defence(value)
            case "armour" | "armor":
                result["armour"] = assign_armour(value)
            case "notes":
                result["notes"] = value
            case _:
                # this is the catch-all, if we get here the label
                # did not match any of the known values and we should
                # print something!
                print(
                    f"There was a problem extracting the label\n"
                    f"{line=}\n"
                    f"{label=}\n"
                    f"{value=}\n"
                )

    return result
