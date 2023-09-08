import os
import random
import pygame
from classes.window import Window


class MainMenu(Window):
    def __init__(self, player) -> None:
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
            "Characters (C)",
            "Workshop (W)",
            "Summon (S)",
            "Pocket (P)",
        ]
        img_path = "assets/light_gray.png"

        for opt in options:
            start_x = 1 / 26 * self.WIDTH
            start_y = 1 / 8 * (options.index(opt) + 2) * self.HEIGHT - (
                1 / 10 * self.HEIGHT + self.WIDTH * 0.04
            )
            width = 1 / 3 * self.WIDTH
            height = 1 / 10 * self.HEIGHT

            profile_img = self.load_and_resize_image(img_path, width, height)
            self.screen.blit(profile_img, (start_x, start_y))
            self.draw_rect_lines(
                self.DARK_GRAY, start_x, start_y, start_x + width, start_y + height, 5
            )

            text_surface = self.render_text(opt, int(self.WIDTH * 0.04), self.DARK_GRAY)
            self.blit_text(
                text_surface,
                1 / 15 * self.WIDTH,
                1 / 8 * (options.index(opt) + 1) * self.HEIGHT,
            )
        return

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        print("summon")
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
