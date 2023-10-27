import pygame
import math
from pygame.locals import *
from datetime import datetime
from preferences import *
from watches_hand import *

class MechanicalWatches:

    def __init__(self) -> None:
        pygame.init()

        self.__window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        self.__running = True
        self.__clock = pygame.time.Clock()

        self.__sys_font = pygame.font.SysFont(None, 24)
        self.__bg_image = pygame.image.load(BACKGROUND_IMAGE_PATH)
        self.__bg_image = pygame.transform.scale(
            self.__bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        self.__watches_hands = (
            WatchesHand(
                self.__window,
                thickness = HOURS_HAND_THICKNESS,
                degrees_step = HOURS_HAND_DEGREES_STEP,
                length = HOURS_HAND_LENGTH,
                color = BLACK_COLOR
            ),
            WatchesHand(
                self.__window,
                thickness = MINUTES_HAND_THICKNESS,
                degrees_step = MINUTES_HAND_DEGREES_STEP,
                length = MINUTES_HAND_LENGTH,
                color = BLACK_COLOR
            ),
            WatchesHand(
                self.__window,
                thickness = SECONDS_HAND_THICKNESS,
                degrees_step = SECONDS_HAND_DEGREES_STEP,
                length = SECONDS_HAND_LENGTH,
                color = BLACK_COLOR
            )
        )
        
    def run(self) -> None:
        while self.__running:
            self.__current_time = self.__get_current_time()

            self.__window.blit(self.__bg_image, (0, 0))

            self.__process_events()
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
        pygame.draw.circle(
            self.__window, 
            WHITE_COLOR, 
            (WINDOW_HALF_WIDTH, WINDOW_HALF_HEIGHT), 
            WATCHES_BG_RADIUS
        )

        # Watches edge
        pygame.draw.circle(
            self.__window, 
            BLACK_COLOR, 
            (WINDOW_HALF_WIDTH, WINDOW_HALF_HEIGHT), 
            WATCHES_BG_RADIUS,
            WATCHES_BG_EDGE_THICKNESS
        )

        # TODO: Time cuttoffs

        # Watches hands
        for tci in range(len(self.__current_time)):
            self.__watches_hands[tci].draw(self.__current_time[tci])

        # Watches middle
        pygame.draw.circle(
            self.__window,
            BLACK_COLOR,
            (WINDOW_HALF_WIDTH, WINDOW_HALF_HEIGHT),
            WATCHES_MIDDLE_CIRCLE_RADIUS
        )

    def __get_current_time(self) -> tuple:
        now_datetime = datetime.now()
        tt = now_datetime.timetuple()

        return (tt.tm_hour, tt.tm_min, tt.tm_sec)

