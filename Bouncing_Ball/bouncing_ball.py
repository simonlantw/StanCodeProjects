"""
File: bouncing_ball.py
Name: Simon Lan
-------------------------
A ball will start bouncing after user clicked the mouse
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')
temp = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    window.add(ball)
    global temp
    onmouseclicked(start)
    vy = count = 0

    while True:
        if temp is True and count < 3:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y + ball.height > window.height:  # ball hits the ground
                if vy > 0:
                    vy *= -REDUCE
            if ball.x > window.width:  # ball falls out of window
                ball.x = START_X
                ball.y = START_Y
                vy = 0
                temp = False
                count += 1
        pause(DELAY)


def start(event):
    global temp
    temp = True


if __name__ == "__main__":
    main()
