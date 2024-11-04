"""
File: draw_line.py
Name: Quill
-------------------------
This file creates lines on an instance of GWindow class.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousedragged, onmousemoved

# This constant controls the size of the GOval
SIZE = 5

# Global Variable
window = GWindow()
run = 0  # Tracks for the first or second click
click = 0   # Stores the first click


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    """
    A line appears at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    global run, click
    if run == 0:
        pen_stroke = GOval(SIZE, SIZE)
        pen_stroke.filled = False
        window.add(pen_stroke, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        click = pen_stroke    # Store the GOval object
        run += 1    # Update the state to wait for the second click
    else:
        line = GLine(click.x, click.y, mouse.x, mouse.y)
        window.add(line)
        window.remove(click)
        run = 0   # Reset the state for the next first click


if __name__ == "__main__":
    main()
