"""Snake game."""

import curses
import random
import time
from dataclasses import dataclass
from enum import Enum
from typing import List


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

    def __init__(self, x: int, y: int, dir: Direction):
        self.pos = [Pos(x, y)]

        self.prev_tail_pos = Pos(x, y)

        self.dir = dir  # Direction

    def head_pos(self) -> Pos:
        return self.pos[0]

    def body_pos(self) -> List[Pos]:
        return self.pos[1:]

    def change_dir(self, dir: Direction) -> None:
        """Change player's current direction."""
        # Refuse moving to the previous head's position
        if (
            len(self.pos) > 1
            and self.dir == Direction.UP
            and dir == Direction.DOWN
            or self.dir == Direction.DOWN
            and dir == Direction.UP
            or self.dir == Direction.LEFT
            and dir == Direction.RIGHT
            or self.dir == Direction.RIGHT
            and dir == Direction.LEFT
        ):
            return

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
            self.head_pos().y -= 1
        elif self.dir == Direction.DOWN:
            self.head_pos().y += 1
        elif self.dir == Direction.LEFT:
            self.head_pos().x -= 1
        elif self.dir == Direction.RIGHT:
            self.head_pos().x += 1

    def get_food(self, food_pos) -> bool:
        """Check whether a player get a food."""
        return self.head_pos() == food_pos

    def extend(self) -> None:
        """Extend a body."""
        self.pos.append(Pos(self.prev_tail_pos.x, self.prev_tail_pos.y))

    def collide(self, wall_pos) -> bool:
        """Check collision."""
        # Check collision to my body
        if self.head_pos() in self.body_pos():
            return True

        # Check collision to walls
        if self.head_pos() in wall_pos:
            return True

        return False

    def print(self, scr: curses.window) -> None:
        """Print a player."""
        # Cleer the previous tail
        scr.addstr(self.prev_tail_pos.y, self.prev_tail_pos.x, " ")

        # Print a head, change by the current direction
        if self.dir == Direction.UP:
            scr.addstr(
                self.head_pos().y, self.head_pos().x, "A", curses.color_pair(2)
            )
        elif self.dir == Direction.DOWN:
            scr.addstr(
                self.head_pos().y, self.head_pos().x, "v", curses.color_pair(2)
            )
        elif self.dir == Direction.LEFT:
            scr.addstr(
                self.head_pos().y, self.head_pos().x, "<", curses.color_pair(2)
            )
        else:  # Direction.RIGHT
            scr.addstr(
                self.head_pos().y, self.head_pos().x, ">", curses.color_pair(2)
            )

        # Print a body
        for i in range(1, len(self.pos)):
            scr.addstr(self.pos[i].y, self.pos[i].x, "O", curses.color_pair(2))


class Map:
    """Map object."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        # Set walls
        self.wall_pos = []
        for y in range(self.height):
            self.wall_pos.append(Pos(0, y))
            self.wall_pos.append(Pos(self.width - 1, y))
        for x in range(1, self.width - 1):
            self.wall_pos.append(Pos(x, 0))
            self.wall_pos.append(Pos(x, self.height - 1))

    def print(self, scr: curses.window) -> None:
        """Print a map."""

        for pos in self.wall_pos:
            scr.addstr(pos.y, pos.x, "X", curses.color_pair(1))


class Food:
    """Food object."""

    def __init__(self):
        self.pos = Pos(0, 0)

    def put_random(
        self,
        width: int,
        height: int,
        wall_pos: List[Pos],
        player_pos: List[Pos],
    ) -> None:
        """Put a food in random place in a stage."""
        # Get free positions in the map
        free_pos = []
        for y in range(height):
            for x in range(width):
                pos = Pos(x, y)
                if pos not in wall_pos and pos not in player_pos:
                    free_pos.append(pos)

        i = random.randrange(len(free_pos))
        self.pos.x = free_pos[i].x
        self.pos.y = free_pos[i].y

    def print(self, scr: curses.window) -> None:
        """Print a food."""
        scr.addstr(self.pos.y, self.pos.x, "O", curses.color_pair(3))


def main(stdscr: curses.window) -> None:
    """Main loop."""
    # Don't display a cursor
    curses.curs_set(0)

    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Walls
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Player
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Food

    # Use non-blocking mode
    stdscr.nodelay(True)

    STAGE_WIDTH = 24
    STAGE_HEIGHT = 12

    # Initialize objects
    player = Player(STAGE_WIDTH // 2, STAGE_HEIGHT // 2, Direction.UP)
    player.print(stdscr)

    map = Map(STAGE_WIDTH, STAGE_HEIGHT)
    map.print(stdscr)

    random.seed()

    food = Food()
    food.put_random(map.width, map.height, map.wall_pos, player.pos)
    food.print(stdscr)

    # Waiting time for player input
    wait_duration = 0.4
    wait_sec = wait_duration
    REDUCING_WAIT_DURATION = 0.01

    SEC_PER_FRAME = 0.033

    score = 0

    while True:
        # Input
        key = stdscr.getch()

        # Move a player
        if key == ord("w") or key == curses.KEY_UP:
            player.change_dir(Direction.UP)
        elif key == ord("s") or key == curses.KEY_DOWN:
            player.change_dir(Direction.DOWN)
        elif key == ord("a") or key == curses.KEY_LEFT:
            player.change_dir(Direction.LEFT)
        elif key == ord("d") or key == curses.KEY_RIGHT:
            player.change_dir(Direction.RIGHT)

        # Quit the game
        if key == ord("q"):
            break

        # Move a player after waiting
        if wait_sec <= 0:
            player.move()
            player.print(stdscr)
            wait_sec = wait_duration

        if player.get_food(food.pos):
            # Extend the player's body
            player.extend()

            # And put a food in new place
            food.put_random(map.width, map.height, map.wall_pos, player.pos)
            food.print(stdscr)

            # Speed up the game
            if wait_duration >= SEC_PER_FRAME:
                wait_duration -= REDUCING_WAIT_DURATION
            else:
                wait_duration = SEC_PER_FRAME

            score += 1

        stdscr.addstr(0, 0, f"Score: {score} ")

        if player.collide(map.wall_pos):
            # Game over
            str = "GAMEOVER"
            stdscr.addstr(
                STAGE_HEIGHT // 2, STAGE_WIDTH // 2 - len(str) // 2, str
            )
            stdscr.refresh()
            time.sleep(2)
            break

        stdscr.refresh()

        # Wait for a frame (rough 30[fps])
        time.sleep(SEC_PER_FRAME)
        wait_sec -= SEC_PER_FRAME


if __name__ == "__main__":
    # Wrapper for curses initialization and finalization
    curses.wrapper(main)
