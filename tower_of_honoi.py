"""
MODULE: tower_of_honoi
AUTHOR: Jeff Alkire
DATE:   April 6, 2023

I ran across the statement that the Tower of Honoi puzzle could be solved with a recursive algorithm while
reading a book.  I love puzzles and recursion is fun, so I skipped the solution and decided to try it for
myself.  Here is the result displayed to a text terminal.

Usage:
    tower-of-honoi [size] [q|Q]
        [size] and [q|Q] are optional parameters.
        size indicates the number of tiles in the puzzle
        q|Q  a case-insensitive letter q indicating to use quiet mode.  In quiet mode, the puzzle is solved
                and each step is output to the screen.  In default mode, the user is prompted for a key between
                each step in the solution.

Example:
    tower-of-honoi 3

    will start with:
               ||          ||          ||
               ||          ||          ||
              ====         ||          ||
             ======        ||          ||
            ========       ||          ||

    and end with:
               ||          ||          ||
               ||          ||          ||
               ||          ||         ====
               ||          ||        ======
               ||          ||       ========

"""
import pynput
import sys
import time

import peg


class Const:
    """ Constants for this module."""
    DEFAULT_SIZE = 6
    QUIET = False


def print_pegs(pegs: [peg.TowerPeg]):
    """
    Display the puzzle's 3 pegs.
    Example display:
                  ||                ||                ||
                  ||                ||                ||
                  ||                ||                ||
                  ||                ||                ||
                  ||                ||                ||
                  ||               ====               ||
                  ||              ======         ============
              ==========         ========       ==============

    pegs: the 3 pegs of the puzzle.
    """
    def key_released(_):
        """ Simple fn to return False when a keypress is released. """
        return False

    height = pegs[0].peg_height
    for idx in range(height):
        print("    ", end="")
        for p in pegs:
            p.print_line(idx)
            print("    ", end="")
        print()
    print()

    if not Const.QUIET:
        print("    Press any key to continue ...")

        # Loop until a key is pressed and released
        with pynput.keyboard.Listener(on_release=key_released) as listen:
            listen.join()
            print("", end="")
    else:
        print()
        time.sleep(0.250)
    print()


def usage():
    """ Display program usage and exit the program. """
    print()
    print("Usage:")
    print("    tower-of-honoi [tower size] [q]")
    print("        tower size = number of tiles in the tower.  (Defaults to 6)")
    print("        q | Q      = quiet mode.  (Do not ask for keypress between moves)")
    print()
    sys.exit()


def move_coaster(from_peg: peg.TowerPeg, to_peg: peg.TowerPeg) -> None:
    """
    Move a tile/coaster from one peg to another peg.
    param from_peg: Peg to remove the tile from.
    param to_peg: Peg to add the tile to.
    """
    coaster: int = from_peg.remove_from_top()
    to_peg.add_to_top(coaster)


def solve(pegs: [peg.TowerPeg],
          first_peg: peg.TowerPeg,
          extra_peg: peg.TowerPeg,
          last_peg: peg.TowerPeg,
          depth: int
          ) -> int:
    """
    Recursive function to solve a piece of the puzzle
    param pegs: a list of 3 pegs in the order they are to be displayed on the screen.
    param first_peg: The location of a stack of tiles that are to be moved.
    param extra_peg: A peg used during the movement.  At the end of the move, it
                        will have the same contents as it did at the start.
    param last_peg: The location the stack of tiles should be moved to.
    param depth: The number of tiles that are to be moved.
    return: The number of moves it took to solve this portion of the puzzle
    """
    if 2 == depth:
        move_coaster(first_peg, extra_peg)
        print_pegs(pegs)
        move_coaster(first_peg, last_peg)
        print_pegs(pegs)
        move_coaster(extra_peg, last_peg)
        print_pegs(pegs)
        return 3
    else:
        # Move those tiles from the first peg to the extra peg.
        early_moves = solve(pegs, first_peg, last_peg, extra_peg, depth-1)

        # Move the last tile to the solved peg
        move_coaster(first_peg, last_peg)
        print_pegs(pegs)

        # Move the stack in the extra peg to the solved peg.
        late_moves = solve(pegs, extra_peg, first_peg, last_peg, depth-1)
        return early_moves + 1 + late_moves


def main():
    """
    Main body of tower_of_honoi routine. Reads the command line, sets up the pegs and calls solve().
    """
    sz = 0
    for n in range(len(sys.argv)):
        if sys.argv[n].upper()[0] == "Q":
            Const.QUIET = True
    if len(sys.argv) > 1 and sys.argv[1].upper()[0] != "Q":
        try:
            sz = int(sys.argv[1])
        except ValueError:
            print()
            print(f"{sys.argv[1]} is not an integer.  Tower size must be an integer.")
            print(f"    Using default value of {Const.DEFAULT_SIZE}.")
            usage()
    else:
        sz = Const.DEFAULT_SIZE

    print()
    print()
    pegs: [peg.TowerPeg] = [peg.TowerPeg(sz, True), peg.TowerPeg(sz), peg.TowerPeg(sz)]

    print_pegs(pegs)
    moves = solve(pegs, pegs[0], pegs[1], pegs[2], sz)
    print()
    print(f"Solved in {moves} moves.")


if "__main__" == __name__:
    main()
