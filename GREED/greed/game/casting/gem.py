import random
from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

from game.shared.color import Color
from game.shared.point import Point


class Gem(Actor):
    """A gem that is in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

    def __init__(self): #, cols, rows, cell_size, font_size):
        """Constructs a new Actor."""
        # x = random.randint(1, cols - 1)
        # y = random.randint(1, rows - 1)
        # position = Point(x, y)
        # position = position.scale(cell_size)

        # r = random.randint(0, 255)
        # g = random.randint(0, 255)
        # b = random.randint(0, 255)
        # color = Color(r, g, b)
        
        # self.set_text( "*")
        # self.set_font_size(font_size)
        # self.set_color(color)
        # self.set_position(position)
        
