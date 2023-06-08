from dataclasses import dataclass
from enum import IntEnum, StrEnum


class RandOptDifficulty(IntEnum):
    EASY = 0
    MEDIUM = 1
    HARD = 2

    @property
    def description(self):
        match self:
            case self.EASY:
                return "Fair"
            case self.MEDIUM:
                return "Unfair"
            case self.HARD:
                return "Very Unfair"
            case _:
                raise ValueError(f"Invalid Difficulty: {self}")


class RandOptKeyDifficulty(IntEnum):
    LEAVE_ALONE = 0
    RANDOMIZE = 1
    RACE_MODE = 2
    SPEEDRUN_MODE = 3

    @property
    def description(self):
        match self:
            case self.LEAVE_ALONE:
                return "Not Shuffled"
            case self.RANDOMIZE:
                return "Shuffled"
            case self.RACE_MODE:
                return "Race Mode"
            case self.SPEEDRUN_MODE:
                return "Race Mode +"
            case _:
                raise ValueError(f"Invalid Shuffle Mode: {self}")


class RandOptStartItemsDifficulty(IntEnum):
    SHIELD_AND_1H = 0
    SHIELD_AND_2H = 1
    COMBINED_POOL_AND_2H = 2

    @property
    def description(self):
        match self:
            case self.SHIELD_AND_1H:
                return "Shield & 1H Weapon"
            case self.SHIELD_AND_2H:
                return "Shield & 1/2H Weapon"
            case self.COMBINED_POOL_AND_2H:
                return "Shield/Weapon & Weapon"
            case _:
                raise ValueError(f"Invalid Starter Weapons Combination: {self}")


class RandOptSoulItemsDifficulty(IntEnum):
    SHUFFLE = 0
    CONSUMABLE = 1
    TRANSPOSE = 2

    @property
    def description(self):
        match self:
            case self.SHUFFLE:
                return "Shuffled"
            case self.CONSUMABLE:
                return "Replaced"
            case self.TRANSPOSE:
                return "Transposed"
            case _:
                raise ValueError(f"Invalid Soul Item Shuffle Setting: {self}")


class RandOptGameVersion(StrEnum):
    PTDE = "DARK SOULS: Prepare To Die Edition"
    REMASTERED = "DARK SOULS: REMASTERED"


@dataclass
class RandomizerOptions:
    difficulty: RandOptDifficulty
    fashion_souls: bool
    key_placement: RandOptKeyDifficulty
    use_lordvessel: bool
    use_lord_souls: bool
    soul_items_diff: RandOptSoulItemsDifficulty
    start_items_diff: RandOptStartItemsDifficulty
    game_version: RandOptGameVersion
    randomize_npc_armor: bool

    @staticmethod
    def bool_option_to_string(option: bool) -> str:
        return "On" if option else "Off"

    def __str__(self):
        return (
            f"Randomizer Settings:\n"
            f"  Game Version: {self.game_version}\n"
            f"  Difficulty: {self.difficulty.description}\n"
            f"  Fashion Souls: {self.bool_option_to_string(self.fashion_souls)}\n"
            f"  Key Difficulty: {self.key_placement.description}\n"
            f"  Senile Gwynevere: {self.bool_option_to_string(self.use_lordvessel)}\n"
            f"  Senile Primordial Serpents: {self.bool_option_to_string(self.use_lord_souls)}\n"
            f"  Soul Items: {self.soul_items_diff.description}\n"
            f"  Starting Items: {self.start_items_diff.description}\n"
            f"  Laundromat Mixup: {self.bool_option_to_string(self.randomize_npc_armor)}\n"
        )

    def as_string(self) -> str:
        return str(self)
