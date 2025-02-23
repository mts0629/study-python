"""Snake game."""

import curses
import random
import time
from enum import Enum
from dataclasses import dataclass


@dataclass
class Pos:
    """2-d coordinates (x, y)."""

    x: int
    y: int


class Direction(Enum):
    """Direction to move."""

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Player:
    """Player object."""

    def __init__(self, x, y, dir):
        self.pos = [Pos(x, y)]
        self.head_pos = self.pos[0]

        self.prev_tail_pos = Pos(x, y)

        self.dir = dir  # Direction

    def change_dir(self, dir) -> None:
        """Change player's current direction."""
        self.dir = dir

    def move(self) -> None:
        """Move a player."""
        # Copy the previous tail
        self.prev_tail_pos.x = self.pos[-1].x
        self.prev_tail_pos.y = self.pos[-1].y

        # Move a body
        for i in range(len(self.pos) - 1, 0, -1):
            self.pos[i].x = self.pos[i - 1].x
            self.pos[i].y = self.pos[i - 1].y

        # Move a head
        if self.dir == Direction.UP:
            self.head_pos.y -= 1
        elif self.dir == Direction.DOWN:
            self.head_pos.y += 1
        elif self.dir == Direction.LEFT:
            self.head_pos.x -= 1
        elif self.dir == Direction.RIGHT:
            self.head_pos.x += 1

    def get_food(self, food) -> bool:
        """Check whether a player get a food."""
        return self.head_pos == food.pos

    def extend(self) -> None:
        """Extend a body."""
        self.pos.append(Pos(self.prev_tail_pos.x, self.prev_tail_pos.y))

    def collide(self, map) -> bool:
        """Check collision."""
        # Check collision between my body
        for i in range(1, len(self.pos)):
            if self.head_pos == self.pos[i]:
                return True

        # Check collision between walls
        if map.get_chip(self.head_pos) == 1:
            return True

        return False

    def print(self, scr) -> None:
        """Print a player."""
        # Cleer the previous tail
        scr.addstr(self.prev_tail_pos.y, self.prev_tail_pos.x, " ")

        # Print a head, change by the current direction
        if self.dir == Direction.UP:
            scr.addstr(self.head_pos.y, self.head_pos.x, "A")
        elif self.dir == Direction.DOWN:
            scr.addstr(self.head_pos.y, self.head_pos.x, "V")
        elif self.dir == Direction.LEFT:
            scr.addstr(self.head_pos.y, self.head_pos.x, "<")
        else:  # Direction.RIGHT
            scr.addstr(self.head_pos.y, self.head_pos.x, ">")

        # Print a body
        for i in range(1, len(self.pos)):
            scr.addstr(self.pos[i].y, self.pos[i].x, "O")


class Map:
    """Map object."""

    def __init__(self, width: int, height: int):
        self.grid = [0] * width * height
        self.width = width
        self.height = height

        # Set walls
        for y in range(self.height):
            self.grid[y * self.width] = 1
            self.grid[y * self.width + self.width - 1] = 1
        for x in range(1, self.width - 1):
            self.grid[x] = 1
            self.grid[(self.height - 1) * self.width + x] = 1

    def get_chip(self, pos):
        """Get a map chip."""
        return self.grid[pos.y * self.width + pos.x]

    def print(self, scr) -> None:
        """Print a map."""
        for i, chip in enumerate(self.grid):
            if chip == 1:
                scr.addstr(i // self.width, i % self.width, "X")


class Food:
    """Food object."""

    def __init__(self):
        self.pos = Pos(0, 0)

    def put_random(self, map):
        """Put a food in random place in a stage."""
        # Get available index in the map
        available_index = [i for i in range(len(map.grid)) if map.grid[i] == 0]
        i = random.randrange(len(available_index))

        self.pos.x = i % map.width
        self.pos.y = i // map.width

    def print(self, scr) -> None:
        """Print a food."""
        scr.addstr(self.pos.y, self.pos.x, "*")


def main(stdscr) -> None:
    """Main loop."""
    # Don't display a cursor
    curses.curs_set(0)

    STAGE_WIDTH = 32
    STAGE_HEIGHT = 16

    # Initialize objects
    player = Player(STAGE_WIDTH // 2, STAGE_HEIGHT // 2, Direction.UP)

    map = Map(STAGE_WIDTH, STAGE_HEIGHT)
    map.print(stdscr)

    random.seed()

    food = Food()
    food.put_random(map)
    food.print(stdscr)

    # Timeout
    frame_ms = 500
    stdscr.timeout(frame_ms)

    # Key
    key = None
    while True:
        # Move a player by key input
        if key == ord("w"):
            player.change_dir(Direction.UP)
        elif key == ord("s"):
            player.change_dir(Direction.DOWN)
        elif key == ord("a"):
            player.change_dir(Direction.LEFT)
        elif key == ord("d"):
            player.change_dir(Direction.RIGHT)
        elif key == ord("q"):
            # Quit the game
            break

        player.move()

        if player.get_food(food):
            # Extend the player's body and replace the food
            player.extend()
            food.put_random(map)
            food.print(stdscr)

        if player.collide(map):
            # Game over
            str = "GAMEOVER"
            stdscr.addstr(
                STAGE_HEIGHT // 2, STAGE_WIDTH // 2 - len(str) // 2, str
            )
            stdscr.refresh()
            time.sleep(1)
            break

        player.print(stdscr)

        stdscr.refresh()

        # Input
        key = stdscr.getch()


if __name__ == "__main__":
    # Wrapper for curses initialization and finalization
    curses.wrapper(main)
