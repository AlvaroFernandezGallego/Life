"""
Rule system for Life-like cellular automata.

Supports rules in format:

    SURVIVAL/BIRTH

Examples:
    23/3   -> Conway's Life
    23/36  -> HighLife
    16/6   -> Custom rule
"""


class LifeRule:
    """
    Represents a Life-like cellular automaton rule.
    """

    def __init__(self, survival, birth):
        """
        Initialize rule.

        Args:
            survival: Iterable of survival neighbor counts.
            birth: Iterable of birth neighbor counts.
        """
        self.survival = set(survival)
        self.birth = set(birth)

    @classmethod
    def from_string(cls, rule_string: str):
        """
        Parse rule from string.

        Args:
            rule_string: Rule in SURVIVAL/BIRTH format.

        Returns:
            LifeRule instance.
        """
        try:
            survival_part, birth_part = rule_string.split("/")
        except ValueError:
            raise ValueError("Rule must be in format 'SURVIVAL/BIRTH'")

        survival = {int(n) for n in survival_part}
        birth = {int(n) for n in birth_part}

        return cls(survival, birth)

    def should_survive(self, neighbors: int) -> bool:
        """Return True if alive cell survives."""
        return neighbors in self.survival

    def should_be_born(self, neighbors: int) -> bool:
        """Return True if dead cell becomes alive."""
        return neighbors in self.birth