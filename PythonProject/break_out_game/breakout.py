"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        vx = graphics.get_dx()    # Get dx
        vy = graphics.get_dy()    # Get dy
        if graphics.start():    # Check if the switch is Ture
            graphics.ball.move(vx, vy)
            graphics.bouncing(graphics.ball)
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.reverse_dx()
            if graphics.ball.y <= 0:
                graphics.reverse_dy()
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                if lives == 0:
                    graphics.reset_ball()
                    graphics.game_over()
                    break   # exit loop if no lives
                else:
                    graphics.reset_ball()
                    graphics.stop()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
