import pygame
import math
from pygame.locals import *
from datetime import datetime
from preferences import *

class MechanicalWatches:

    __running = True
    
    def __init__(self) -> None:
        pygame.init()

        self.__window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        self.__clock = pygame.time.Clock()
        self.__sys_font = pygame.font.SysFont(None, 24)
        
    def run(self) -> None:
        while self.__running:
            self.__current_time = self.__get_current_time()
            self.__process_events()
            # Set background color
            self.__window.fill(YELLOW_COLOR)
            
            self.__draw_objects()

            pygame.display.flip()

            self.__clock.tick(FPS)

        pygame.quit()

    def __process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.__running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.__running = False

    def __draw_objects(self) -> None:
        # Watches background
        watches_bg_radius= int(WINDOW_HALF_HEIGHT * 0.9)
        pygame.draw.circle(
            self.__window, 
            RED_COLOR, 
            (WINDOW_HALF_WIDTH, WINDOW_HALF_HEIGHT), 
            watches_bg_radius
        )

        # Seconds arrow
        self.__draw_clock_hand(
            watches_bg_radius,
            GREEN_COLOR,
            3,
            self.__current_time[2],
            6,
            WINDOW_HALF_HEIGHT,
            WINDOW_HALF_WIDTH
        )

        # Minutes arrow
        self.__draw_clock_hand(
            watches_bg_radius, 
            PINK_COLOR, 
            6, 
            self.__current_time[1], 
            6,
            WINDOW_HALF_HEIGHT,
            WINDOW_HALF_WIDTH
        )

        # Hours arrow
        self.__draw_clock_hand(
            watches_bg_radius * 0.6, 
            BLUE_COLOR, 
            9, 
            self.__current_time[0], 
            15,
            WINDOW_HALF_HEIGHT,
            WINDOW_HALF_WIDTH
        )

    def __draw_clock_hand(
            self, length: float, color: tuple, thickness: int,
            time: int, degrees: int, x_offset: float, y_offset: float
        ) -> None:
        end_point = self.__get_arrow_end_point(time, degrees)
        pygame.draw.line(
            self.__window, 
            color, 
            (WINDOW_HALF_WIDTH, WINDOW_HALF_HEIGHT),
            (
                length * end_point[0] + y_offset, 
                length * end_point[1] + x_offset
            ),
            thickness
        )

    def __get_arrow_end_point(self, time_value: int, degrees: int) -> tuple:
        radians = -(time_value * degrees * math.pi / 180.0) - math.pi

        return (math.sin(radians), math.cos(radians))

    def __get_current_time(self) -> tuple:
        now_datetime = datetime.now()
        tt = now_datetime.timetuple()

        return (tt.tm_hour, tt.tm_min, tt.tm_sec)

