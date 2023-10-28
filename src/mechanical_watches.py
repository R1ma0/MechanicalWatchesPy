import pygame
import math
from pygame.locals import *
from datetime import datetime
from preferences import *
from watches_line import *

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

        self.__create_watches_arrows()

    def run(self) -> None:
        while self.__running:
            self.__current_time = self.__get_current_time()

            self.__window.blit(self.__bg_image, (0, 0))

            self.__process_events()
            self.__draw_objects()

            pygame.display.flip()

            self.__clock.tick(FPS)

        pygame.quit()

    def __create_watches_arrows(self):
        self.__watches_hands = (
            WatchesLine(
                self.__window,
                HOURS_HAND_THICKNESS,
                HOURS_HAND_DEGREES_STEP,
                HOURS_HAND_COLOR,
                0,
                HOURS_HAND_LENGTH
            ),
            WatchesLine(
                self.__window,
                MINUTES_HAND_THICKNESS,
                MINUTES_HAND_DEGREES_STEP,
                MINUTES_HAND_COLOR,
                0,
                MINUTES_HAND_LENGTH
            ),
            WatchesLine(
                self.__window,
                SECONDS_HAND_THICKNESS,
                SECONDS_HAND_DEGREES_STEP,
                SECONDS_HAND_COLOR,
                0,
                SECONDS_HAND_LENGTH
            )
        )

        self.__sec_min_cuttoffs = []

        for ct in range(0, 60, 1): # ct - cuttoff time value
            if ct % 5 == 0:
                continue

            self.__sec_min_cuttoffs.append(
                WatchesLine(
                    self.__window,
                    SEC_MIN_CUTTOFFS_THICKNESS,
                    SECONDS_HAND_DEGREES_STEP,
                    SEC_MIN_CUTTOFFS_COLOR,
                    SEC_MIN_CUTTOFFS_START_POS,
                    SEC_MIN_CUTTOFFS_END_POS,
                    ct
                )   
            )

        self.__hours_cuttoffs = []

        for ct in range(0, 60, 1):
            if ct % 5 != 0:
                continue

            self.__hours_cuttoffs.append(
                WatchesLine(
                    self.__window,
                    HOURS_CUTTOFFS_THICKNESS,
                    HOURS_HAND_DEGREES_STEP,
                    HOURS_CUTTOFFS_COLOR,
                    HOURS_CUTTOFFS_START_POS,
                    HOURS_CUTTOFFS_END_POS,
                    ct
                )   
            )

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
            WATCHES_BG_COLOR, 
            (WINDOW_HALF_WIDTH, WINDOW_HALF_HEIGHT), 
            WATCHES_BG_RADIUS
        )

        # Watches edge

        pygame.draw.circle(
            self.__window, 
            WATCHES_EDGE_COLOR, 
            (WINDOW_HALF_WIDTH, WINDOW_HALF_HEIGHT), 
            WATCHES_BG_RADIUS,
            WATCHES_BG_EDGE_THICKNESS
        )

        # Cuttoffs

        for sec_min_cuttoff in self.__sec_min_cuttoffs:
            sec_min_cuttoff.draw()

        for hour_cuttoff in self.__hours_cuttoffs:
            hour_cuttoff.draw()

        # Watches hands

        for tci in range(len(self.__current_time)):
            self.__watches_hands[tci].draw(self.__current_time[tci])

        # Watches middle

        pygame.draw.circle(
            self.__window,
            WATCHES_MIDDLE_COLOR,
            (WINDOW_HALF_WIDTH, WINDOW_HALF_HEIGHT),
            WATCHES_MIDDLE_CIRCLE_RADIUS
        )

    def __get_current_time(self) -> tuple:
        now_datetime = datetime.now()
        tt = now_datetime.timetuple()

        return (tt.tm_hour, tt.tm_min, tt.tm_sec)

