"""
Name: Wiley Lin
This constructor defines all the setting of the game, breakout.
"""
from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved
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
    """
    This function creates the surface that user can play a game called breakout.
    There are a number of bricks, a ball, and one paddle.
    """

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle_width = PADDLE_WIDTH
        self.paddle_height = PADDLE_HEIGHT
        self.paddle.color = "BLACK"
        self.paddle.filled = True
        self.paddle.fill_color = "BLACK"
        self.window.add(self.paddle, self.window_width//2-paddle_width//2, self.window_height - paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2)
        self.ball_radius = BALL_RADIUS
        self.ball.color = "BLACK"
        self.ball.filled = "BLACK"
        self.ball.fill_color = "BLACK"
        self.window.add(self.ball, self.window_width//2-BALL_RADIUS//2, self.window_height//2-BALL_RADIUS//2)
        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx
        self.__dy = INITIAL_Y_SPEED
        self.frame_rate = 10
        # # Initialize our mouse listeners
        onmousemoved(self.change_position)

        # Draw bricks
        self.bricks_number = 0
        for i in range(0, BRICK_ROWS, 1):
            for j in range(0, BRICK_COLS, 1):
                self.bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.bricks.filled = True
                if BRICK_COLS > BRICK_ROWS:
                    if i < 2:
                        self.bricks.color = "THISTLE"
                        self.bricks.fill_color = "THISTLE"
                    if 4 > i >= 2:
                        self.bricks.color = "SIENNA"
                        self.bricks.fill_color = "SIENNA"
                    if 6 > i >= 4:
                        self.bricks.color = "THISTLE"
                        self.bricks.fill_color = "THISTLE"
                    if 8 > i >= 6:
                        self.bricks.color = "SIENNA"
                        self.bricks.fill_color = "SIENNA"
                    if 10 > i >= 8:
                        self.bricks.color = "THISTLE"
                        self.bricks.fill_color = "THISTLE"
                    self.bricks_number += 1
                    self.window.add(self.bricks, (BRICK_WIDTH + BRICK_SPACING) * j,
                                    BRICK_OFFSET + (BRICK_HEIGHT + BRICK_SPACING) * i)
                else:
                    if i < 2:
                        self.bricks.color = "THISTLE"
                        self.bricks.fill_color = "THISTLE"
                    if 4 > i >= 2:
                        self.bricks.color = "SIENNA"
                        self.bricks.fill_color = "SIENNA"
                    if 6 > i >= 4:
                        self.bricks.color = "THISTLE"
                        self.bricks.fill_color = "THISTLE"
                    if 8 > i >= 6:
                        self.bricks.color = "SIENNA"
                        self.bricks.fill_color = "SIENNA"
                    if 10 > i >= 8:
                        self.bricks.color = "THISTLE"
                        self.bricks.fill_color = "THISTLE"
                    self.bricks_number += 1
                    self.window.add(self.bricks, (BRICK_WIDTH+BRICK_SPACING)*j,
                                    BRICK_OFFSET+(BRICK_HEIGHT+BRICK_SPACING)*i)

    def change_position(self, mouse):
        """
        This function allows the paddle to move with the user's mouse position.
        """
        self.paddle.x = mouse.x - PADDLE_WIDTH/2
        if self.paddle.x + PADDLE_WIDTH > self.window_width:
            self.paddle.x = self.window_width - PADDLE_WIDTH
        if self.paddle.x <= 0:
            self.paddle.x = 0

    def get_dx(self):
        """
        This function returns velocity of x that the ball moves.
        """
        return self.__dx

    def get_dy(self):
        """
        This function returns velocity of y that the ball moves.
        """
        return self.__dy
