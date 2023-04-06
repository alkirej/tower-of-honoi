

class Const:
    """ Constents for the TowerPeg class."""
    PEG_STR: str = "||"


class TowerPeg:
    """
    Class representing a single "peg" in a Tower of Honoi puzzle.  The Tower of Honoi
    typically has 3 such pegs.
    sz: the number of tiles in the puzzle
    start_full: one of the three pegs (usually the first) starts full and the other two start empty.
    """
    def __init__(self, sz: int, start_full: bool = False):
        self.size: int = sz
        self._stack: list = []

        if start_full:
            for n in range(sz, 0, -1):
                self._stack.append(n)

    @property
    def peg_height(self) -> int:
        """ Height of the peg - which is 2 more than the maximum # of tiles in the puzzle. """
        return self.size + 2

    def remove_from_top(self) -> int:
        """
        Remove and return the top tile/coaster from this peg.
        return:  the size of the tile/coaster removed.
        """
        return self._stack.pop()

    def add_to_top(self, coaster_size: int) -> int:
        """
        Add a tile/coaster to the top of this peg
        param coaster_size: the size of the tile/coaster to add to the peg.
        return: the # of tiles currently on this peg after the addition.
        """
        self._stack.append(coaster_size)
        return len(self._stack)

    def print_line(self, line_num: int) -> None:
        """
        Print one "line" of this peg.  The line could have a tile or it could be empty.
        empty tiles will display only the peg.  Non-empty tiles will display the tile/coaster.
        It will have a size according to the size stored in the stack.  It will cover the peg
        and spaces on either side of the peg equal to the size stored in the stack.

        param line_num: the line number (starting with 0 at the top) of the peg portion to display.
                            Any new line characters (which are needed to make the display make
                            sense) are expected to be outside of this method.
        """
        if line_num >= self.peg_height:
            raise ValueError(f"line_num ({line_num}) exceeds tower height ({self.peg_height}).")

        # PRINT PEG ONLY IF LINE IS ABOVE ALL COASTERS ON IT
        if line_num < (self.peg_height - len(self._stack)):
            print(" " * self.size, Const.PEG_STR, " " * self.size, sep="", end="")
        # PRINT THE PROPER SIZE COASTER
        else:
            coaster_size: int = self._stack[self.size - line_num + 1]
            spaces_str: str = " " * (self.size - coaster_size)
            coaster_str_len = 2*coaster_size + len(Const.PEG_STR)
            coaster_str: str = "=" * coaster_str_len
            print(spaces_str, coaster_str, spaces_str, sep="", end="")
