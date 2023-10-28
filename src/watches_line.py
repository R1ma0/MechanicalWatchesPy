import pygame
from math import pi, cos, sin
from preferences import WINDOW_HALF_WIDTH, WINDOW_HALF_HEIGHT

class WatchesLine:

    def __init__(
            self, window, thickness: int, degrees_step: int, color: tuple,
            start_pos: float, end_pos: float, default_time: int = None
        ):
        self.__window = window
        self.__thickness = thickness
        self.__degrees_step = degrees_step
        self.__color = color
        self.__start_pos = start_pos
        self.__end_pos = end_pos
        self.__default_time = default_time

    def draw(self, time: int = None) -> None:
        if time is None and self.__default_time is not None:
            time = self.__default_time

        y, x = self.__calculate_point_coordinates(time)

        pygame.draw.line(
            self.__window, 
            self.__color, 
            (
                self.__start_pos * y + WINDOW_HALF_WIDTH,
                self.__start_pos * x + WINDOW_HALF_HEIGHT
            ),
            (
                self.__end_pos * y + WINDOW_HALF_WIDTH, 
                self.__end_pos * x + WINDOW_HALF_HEIGHT
            ),
            self.__thickness
        )

    def __calculate_point_coordinates(self, time: int) -> tuple:
        radians = -(time * self.__degrees_step * pi / 180.0) - pi

        return (sin(radians), cos(radians))
