import os
import random

from game.casting.actor import Actor
from game.casting.rock import Rock
from game.casting.gem import Gem
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ROCK = 25
DEFAULT_GEMS = 35


def main():
    
    # create the cast
    cast = Cast()
    
    # create the score
    score = Actor()
    score.set_text("Score:0")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("score", score)
    
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y-FONT_SIZE)
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)
    

    for n in range(DEFAULT_ROCK):
        text = "O"
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        rock = Rock()
        rock.set_text(text)
        rock.set_font_size(FONT_SIZE)
        rock.set_color(color)
        rock.set_position(position)

        yspeed = random.randint(1, 5)
        rock.set_velocity(Point(0,yspeed))
        cast.add_actor("rock", rock)
    
    for n in range(DEFAULT_GEMS):
        text = "*"
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        gem = Gem()
        gem.set_text(text)
        gem.set_font_size(FONT_SIZE)
        gem.set_color(color)
        gem.set_position(position)

        yspeed = random.randint(1, 5)
        gem.set_velocity(Point(0,yspeed))
        cast.add_actor("gem", gem)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()