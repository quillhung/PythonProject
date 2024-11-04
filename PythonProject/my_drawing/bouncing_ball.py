"""
File: bouncing_ball.py
Name: Quill
-------------------------
This file show how to simulates a bouncing ball animation by campy library.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constant
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variable
window = GWindow(800, 500, title='bouncing_ball.py')
is_moving = False
run = 0
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(start)


def start(mouse):
    """
    This program simulates a bouncing ball.
    """
    global is_moving, run, ball
    if not is_moving and run < 3:
        is_moving = True   # Change the moving status
        run += 1
        vx = VX
        vy = 0
        while True:
            ball.move(vx, vy)
            # Check if the ball has past the bottom of the window
            if ball.y + ball.height < window.height:
                vy += GRAVITY
            if ball.y + ball.height >= window.height and vy > 0 :
                vy = -vy * REDUCE   # When the ball hits the ground, bouncing
            pause(DELAY)
            # Check if the ball has past the right edge of the window
            if ball.x + ball.width >= window.width:
                break
        window.add(ball, x=START_X, y=START_Y)  # Reset to the initial position
        is_moving = False   # Change the moving status, wait for clicking again


if __name__ == "__main__":
    main()
