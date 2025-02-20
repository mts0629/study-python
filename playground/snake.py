import curses


def main(stdscr) -> None:
    # Clear screen
    stdscr.clear()

    stdscr.addstr("Hello, world!", curses.A_BOLD)

    # Refresh
    stdscr.refresh()

    stdscr.getkey()


if __name__ == "__main__":
    # Wrapper for curses initialization and finalization
    curses.wrapper(main)
