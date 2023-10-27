import pygame
from math import pi, cos, sin
from preferences import WINDOW_HALF_WIDTH, WINDOW_HALF_HEIGHT

class WatchesHand:

    def __init__(
            self, window, thickness: int, degrees_step: int, length: int, 
            color: tuple
        ):
        self.__window = window
        self.__thickness = thickness
        self.__degrees_step = degrees_step
        self.__length = length
        self.__color = color

    def draw(self, time: int) -> None:
        y_end_point, x_end_point = self.__calculate_point_coordinates(time)

        pygame.draw.line(
            self.__window, 
            self.__color, 
            (WINDOW_HALF_WIDTH, WINDOW_HALF_HEIGHT),
            (
                self.__length * y_end_point + WINDOW_HALF_WIDTH, 
                self.__length * x_end_point + WINDOW_HALF_HEIGHT
            ),
            self.__thickness
        )

    def __calculate_point_coordinates(self, time: int) -> tuple:
        radians = -(time * self.__degrees_step * pi / 180.0) - pi

        return (sin(radians), cos(radians))
