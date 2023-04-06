
import pynput
import sys
import time

import peg


class Const:
    DEFAULT_SIZE = 6
    QUIET = False

def print_pegs(pegs: [peg.TowerPeg]):
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
        # while not key_pressed:
        with pynput.keyboard.Listener(on_release=key_released) as listen:
            listen.join()
            print("", end="")
    else:
        print()
        time.sleep(0.250)
    print()


def key_released(_):
    return False


def usage():
    print()
    print("Usage:")
    print("    tower-of-honoi [tower size] [q]")
    print("        tower size = number of tiles in the tower.  (Defaults to 6)")
    print("        q | Q      = quiet mode.  (Do not ask for keypress between moves)")
    print()
    sys.exit()


def main():
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


def move_coaster(from_peg: peg.TowerPeg, to_peg: peg.TowerPeg):
    coaster: int = from_peg.remove_from_top()
    to_peg.add_to_top(coaster)


def solve(pegs: [peg.TowerPeg],
          first_peg: peg.TowerPeg,
          extra_peg: peg.TowerPeg,
          last_peg: peg.TowerPeg,
          depth: int
          ) -> int:

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


if "__main__" == __name__:
    main()
