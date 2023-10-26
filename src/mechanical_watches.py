import pygame
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
    
        # Time 
        current_time = self.__get_current_time()
        time_str = f"{current_time[0]}:{current_time[1]}:{current_time[2]}"
        text = self.__sys_font.render(f"{time_str}", True, RED_COLOR)

        self.__window.blit(text, (10, 10))

    def __get_current_time(self) -> None:
        now_datetime = datetime.now()
        tt = now_datetime.timetuple()

        return (tt.tm_hour, tt.tm_min, tt.tm_sec)

