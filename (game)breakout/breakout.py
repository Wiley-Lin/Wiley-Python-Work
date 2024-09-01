"""
Name: Wiley Lin
This program is a game named breakout.
Skills used in the file: conditional statements, while loops, functions, constructor and user code.
"""
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

graphics = BreakoutGraphics()
vx = graphics.get_dx()
vy = graphics.get_dy()
life = 0


def main():
    """
    This function triggers the game by a mouseclick from the user.
    """
    onmouseclicked(start_game)


def start_game(mouse):
    """
    This function sets the rule of the game, and defines how the ball moves when encountering objects.
    Users have to control the paddle to prevent the ball from falling down to the bottom of the window.
    if the ball drops below the window, then it's game-over.

    Users are allowed to have three tries and if the user breaks all of the bricks when still alive,
    then that user wins the game.
    """
    global vx
    global vy
    global life
    global graphics
    if vx == 0 and vy == 0 and graphics.bricks_number != 0:
        vx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            vx = -vx
        vy = INITIAL_Y_SPEED
    while True:
        if life < 3:
            graphics.ball.move(vx, vy)
            ball_1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            ball_2 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius, graphics.ball.y)
            ball_3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2 * graphics.ball_radius)
            ball_4 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius, graphics.ball.y
                                                    + 2 * graphics.ball_radius)
            if graphics.ball.x + graphics.ball_radius * 2 >= graphics.window_width or graphics.ball.x <= 0:
                vx = -vx
            if graphics.ball.y <= 0:
                vy = -vy
            if ball_1 is graphics.paddle and vy > 0:
                vy = -vy
            if ball_2 is graphics.paddle and vy > 0:
                vy = -vy
            if ball_3 is graphics.paddle and vy > 0:
                vy = -vy
            if ball_4 is graphics.paddle and vy > 0:
                vy = -vy
            if ball_1 is not None and ball_1 is not graphics.paddle:
                vy = -vy
                graphics.bricks_number -= 1
                graphics.window.remove(ball_1)
            if ball_1 is None:
                if ball_2 is not None and ball_2 is not graphics.paddle:
                    vy = -vy
                    graphics.bricks_number -= 1
                    graphics.window.remove(ball_2)
                if ball_2 is None:
                    if ball_3 is not None and ball_3 is not graphics.paddle:
                        vy = -vy
                        graphics.bricks_number -= 1
                        graphics.window.remove(ball_3)
                    if ball_3 is None:
                        if ball_4 is not None and ball_4 is not graphics.paddle:
                            vy = -vy
                            graphics.bricks_number -= 1
                            graphics.window.remove(ball_4)
                        if ball_4 is None:
                            vx = vx
                            vy = vy
            if graphics.bricks_number == 0:
                graphics.window.remove(ball_1)
                graphics.window.remove(ball_2)
                graphics.window.remove(ball_3)
                graphics.window.remove(ball_4)
                vx = 0
                vy = 0
                break
            if graphics.ball.y + graphics.ball_radius * 2 >= graphics.window_height:
                graphics.window.remove(graphics.ball)
                graphics.window.add(graphics.ball, graphics.window_width // 2 - graphics.ball_radius // 2,
                                    graphics.window_height // 2 - graphics.ball_radius // 2)
                life += 1
                vx = 0
                vy = 0
                break
            pause(FRAME_RATE)
        else:
            break


if __name__ == '__main__':
    main()
