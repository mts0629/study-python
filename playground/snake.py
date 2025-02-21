import curses
import time
from enum import Enum


def main(stdscr) -> None:
    """Main loop."""

    class Direction(Enum):
        """Direction to move."""

        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3

    # Initial position and direction
    x = 10
    y = 10
    dir = Direction.UP

    # Key state
    key = None

    # Timeout
    stdscr.timeout(500)

    while True:
        # Clear screen
        stdscr.clear()

        # Input
        if key == curses.KEY_UP:
            dir = Direction.UP
        elif key == curses.KEY_DOWN:
            dir = Direction.DOWN
        elif key == curses.KEY_LEFT:
            dir = Direction.LEFT
        elif key == curses.KEY_RIGHT:
            dir = Direction.RIGHT
        elif key == ord("q"):
            break

        # Move a player
        if dir == Direction.UP:
            y -= 1
        elif dir == Direction.DOWN:
            y += 1
        elif dir == Direction.LEFT:
            x -= 1
        elif dir == Direction.RIGHT:
            x += 1

        if x < 0 or x > curses.COLS - 1 or y < 0 or y > curses.LINES - 1:
            stdscr.insstr(10, 10, "GAME OVER")
            stdscr.refresh()
            time.sleep(1)
            break

        # Print player
        stdscr.insstr(y, x, "O\n")

        # Refresh
        stdscr.refresh()

        # Input
        key = stdscr.getch()


if __name__ == "__main__":
    # Wrapper for curses initialization and finalization
    curses.wrapper(main)
