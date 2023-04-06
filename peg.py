

class Const:
    PEG_STR: str = "||"


class TowerPeg:
    """
    Class representing a single "peg" in a Tower of Honoi puzzle.  The Tower of Honoi
    typically has 3 such pegs.
    """

    def __init__(self, sz: int, start_full: bool = False):
        self.size: int = sz
        self._peg_height: int = sz + 2
        self._stack: list = []

        if start_full:
            for n in range(sz, 0, -1):
                self._stack.append(n)

        self._empty_count: int = self._peg_height - len(self._stack)

    @property
    def peg_height(self):
        return self._peg_height

    def print_by_self(self) -> None:
        print()
        # PRINT EMPTY PORTION OF THE TOWER PEG
        for _ in range(self._peg_height - len(self._stack)):
            print(" " * self.size, "||", " " * self.size)

        for n in reversed(self._stack):
            print(" " * (self.size - n + 1), "=" * (2*n+2), " " * (self.size - n + 1), sep="")

    def num_in_order(self) -> int:
        for idx in range(1, len(self._stack)+1):
            if idx != self._stack[-idx]:
                return idx-1

        return len(self._stack)

    def remove_from_top(self) -> int:
        return self._stack.pop()

    def add_to_top(self, coaster_size: int) -> int:
        self._stack.append(coaster_size)
        return len(self._stack)

    def fits(self, coaster_size: int) -> bool:
        if len(self._stack) == 0:
            return True
        return coaster_size < self._stack[-1]

    def is_empty(self) -> bool:
        return 0 == len(self._stack)

    def top_size(self) -> int:
        if len(self._stack) == 0:
            return self.size + 1
        else:
            return self._stack[-1]

    def stack_size(self) -> int:
        return len(self._stack)

    def print_line(self, line_num: int):
        if line_num >= self._peg_height:
            raise ValueError(f"line_num ({line_num}) exceeds tower height ({self._peg_height}).")

        # PRINT PEG ONLY IF LINE IS ABOVE ALL COASTERS ON IT
        if line_num < (self._peg_height - len(self._stack)):
            print(" " * self.size, Const.PEG_STR, " " * self.size, sep="", end="")
        # PRINT THE PROPER SIZE COASTER
        else:
            coaster_size: int = self._stack[self.size - line_num + 1]
            spaces_str: str = " " * (self.size - coaster_size)
            coaster_str_len = 2*coaster_size + len(Const.PEG_STR)
            coaster_str: str = "=" * coaster_str_len
            print(spaces_str, coaster_str, spaces_str, sep="", end="")
