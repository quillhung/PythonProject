"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT, x=(window_width-paddle_width)/2, y=window_height-PADDLE_OFFSET)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize a switch to track if the ball is moving
        self.switch = False

        # Count bricks
        self.total_bricks = BRICK_ROWS * BRICK_COLS

        # Label show game over
        self.label_lose = GLabel('GAME OVER')

        # Label show you win the game
        self.label_win = GLabel('YOU WIN')

        # Label show how many bricks are left
        self.score_label = GLabel('SCORE: 0')
        self.window.add(self.score_label, x=0, y=self.score_label.height)

        # Initialize our mouse listeners
        onmouseclicked(self.handle_click)
        onmousemoved(self.move_paddle)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=(BRICK_WIDTH+BRICK_SPACING)*i,
                                        y=BRICK_OFFSET+(BRICK_HEIGHT+BRICK_SPACING)*j)
                self.brick.filled = True
                if j // 2 == 0:
                    self.brick.fill_color = self.brick.color = 'red'
                elif j // 2 == 1:
                    self.brick.fill_color = self.brick.color = 'orange'
                elif j // 2 == 2:
                    self.brick.fill_color = self.brick.color = 'yellow'
                elif j // 2 == 3:
                    self.brick.fill_color = self.brick.color = 'green'
                else:
                    self.brick.fill_color = self.brick.color = 'blue'
                self.window.add(self.brick)

    # Move paddle to mouse position
    def move_paddle(self, mouse):
        self.paddle.x = mouse.x - PADDLE_WIDTH / 2
        if self.paddle.x < 0:
            self.paddle.x = 0
        elif self.paddle.x + PADDLE_WIDTH > self.window.width:
            self.paddle.x = self.window.width - PADDLE_WIDTH

    # Start the game when the mouse is clicked
    def handle_click(self, event):
        if not self.switch:
            self.switch = True
            self.set_ball_velocity()

    # Reset the ball position to the center of the window
    def reset_ball(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.switch = False

    # Initialize velocity of the ball
    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # Set bouncing conditions and check for collisions with the paddle or bricks
    def bouncing(self, event):
        obj = self.window.get_object_at(self.ball.x, self.ball.y)
        if obj is not None:
            if obj == self.paddle and self.__dy > 0:
                self.__dy = -self.__dy
            if obj is not self.paddle and obj is not self.score_label:    # To avoid removing paddle
                self.remove_brick(obj)    # Remove the brick
                self.set_ball_velocity()
            return    # Ends the function and return
        obj = self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2)
        if obj is not None:
            if obj == self.paddle and self.__dy > 0:
                self.__dy = -self.__dy
            if obj is not self.paddle and obj is not self.score_label:
                self.remove_brick(obj)
                self.set_ball_velocity()
            return
        obj = self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y)
        if obj is not None:
            if obj == self.paddle and self.__dy > 0:
                self.__dy = -self.__dy
            if obj is not self.paddle and obj is not self.score_label:
                self.remove_brick(obj)
                self.set_ball_velocity()
            return
        obj = self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y + BALL_RADIUS * 2)
        if obj is not None:
            if obj == self.paddle and self.__dy > 0:
                self.__dy = -self.__dy
            if obj is not self.paddle and obj is not self.score_label:
                self.remove_brick(obj)
                self.set_ball_velocity()
            return
        self.you_win()

    # Reverse ball direction
    def reverse_dx(self):
        self.__dx = -self.__dx
        if self.__dx > 0:
            self.__dx += 0.1    # Increase speed to avoid the ball getting stuck in the same trajectory.

    # Reverse ball direction
    def reverse_dy(self):
        self.__dy = -self.__dy
        if self.__dy > 0:
            self.__dy += 0.1    # Increase speed to avoid the ball getting stuck in the same trajectory

    # Get dx
    def get_dx(self):
        return self.__dx

    # Get dy
    def get_dy(self):
        return self.__dy

    # Set switch is False in user
    def start(self):
        return self.switch

    # Change the switch to False while the ball is stopped
    def stop(self):
        self.switch = False

    # Show 'GAME OVER' if no lives
    def game_over(self):
        self.window.add(self.label_lose, x=(self.window.width-self.label_lose.width)/2, y=(self.window.height/2)+50)

    # Show 'YOU WIN' if all bricks has been removed
    def you_win(self):
        if self.total_bricks == 0:
            self.window.add(self.label_win, x=(self.window.width-self.label_win.width)/2, y=(self.window.height/2)+50)
            self.reset_ball()

    # To remove bricks and count score
    def remove_brick(self, obj):
        self.window.remove(obj)
        self.total_bricks -= 1
        removed_bricks = BRICK_ROWS * BRICK_COLS - self.total_bricks
        self.score_label.text = 'SCORE: '+str(removed_bricks)

