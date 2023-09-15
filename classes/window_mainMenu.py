import os
import random
import pygame
from classes.window import Window
from classes.player import Player
from classes.window_floorTest import FloorTest
from classes.window_floorTest_ball import Ball
from classes.window_floorTest_deathmatch import Deathmatch


class MainMenu(Window):
    def __init__(self, player: Player) -> None:
        bg_image_path = self.get_random_bg_image()
        caption = "Main Menu"
        super().__init__(bg_image_path, caption)
        self.player = player

    def get_random_bg_image(self) -> str:
        dir_path = "assets/main_menu"
        images = []
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                images.append(file_path)
        return images[random.randint(0, len(images) - 1)]

    def blit_options(self) -> None:
        options = [
            "Tower (T)",
            "Workshop (W)",
            "Characters (C)",
            "Summon (S)",
            "Next Test (N)",
            "Items (I)",
            "Profile (P)",
            "Options (O)",
            "Log Out (L)",
            "Help (H)",
        ]
        img_path = "assets/light_gray.png"

        for i in range(len(options)):
            if i < 6:
                start_x = 1 / 26 * self.WIDTH
                text_x = 1 / 15 * self.WIDTH
            else:
                start_x = 49 / 78 * self.WIDTH
                text_x = 79 / 120 * self.WIDTH

            width = 1 / 3 * self.WIDTH
            height = 1 / 10 * self.HEIGHT
            start_y = 1 / 20 * (3 * (i % 6) + 1) * self.HEIGHT

            img = self.load_and_resize_image(img_path, width, height)
            self.screen.blit(img, (start_x, start_y))
            self.draw_rect_lines(
                self.DARK_GRAY,
                start_x,
                start_y,
                start_x + width,
                start_y + height,
                3,
            )

            text_surface = self.render_text(
                options[i], int(self.WIDTH * 0.04), self.DARK_GRAY
            )
            self.blit_text(
                text_surface,
                text_x,
                # 1 / 8 * ((i % 6) + 0.7) * self.HEIGHT,
                1 / 20 * (3 * (i % 6) + 1.6) * self.HEIGHT,
            )
        return

    def init_next_test(self) -> (pygame.Surface, FloorTest):
        floor = self.player.floor
        test = self.player.test
        test_window = None

        if floor == 1:
            if test == 1:
                test_window = Ball()
        elif floor == 2:
            if test == 1:
                test_window = Deathmatch()

        if not test_window:
            raise Exception("invalid floor/test number")

        text = f"{test_window.floor}, {test_window.name}"
        popup_text = self.render_text(text, int(self.WIDTH * 0.1), self.LIGHT_GRAY)
        return (popup_text, test_window)

    def popup_loop(self, popup_text) -> bool:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

            self.screen.blit(self.bg_image, (0, 0))
            self.blit_options()
            self.blit_popup()
            self.blit_text(popup_text, 0.5 * self.WIDTH, 0.5 * self.HEIGHT, "center")

            pygame.display.update()
            self.clock.tick(60)
        return True

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        print("tower")
                    if event.key == pygame.K_w:
                        print("workshop")
                    if event.key == pygame.K_c:
                        print("characters")
                    if event.key == pygame.K_s:
                        print("summon")
                    if event.key == pygame.K_n:
                        popup_text, test_window = self.init_next_test()
                        start_level = self.popup_loop(popup_text)
                        if start_level:
                            player_win = test_window.run()
                            if player_win:
                                self.player.advance_to_next_test()
                    if event.key == pygame.K_i:
                        print("items")
                    if event.key == pygame.K_p:
                        print("profile")
                    if event.key == pygame.K_o:
                        print("options")
                    if event.key == pygame.K_l:
                        print("log out")
                    if event.key == pygame.K_h:
                        print("help")
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.screen.blit(self.bg_image, (0, 0))
            self.blit_options()

            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        return
