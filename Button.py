import pygame


class Button:
    def __init__(self, screen, color, weight, height, x, y, action, message, font_name, color_text, type, enabled):
        self.enabled = enabled
        self.scr = screen
        self.color = color
        self.color_text = color_text
        self.weight = weight
        self.height = height
        self.x = x
        self.y = y
        self.action = action
        self.message = message
        self.font_name = font_name
        self.type = type

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        t = self.height
        font = pygame.font.Font(self.font_name, t)

        if self.enabled:
            text_surface = font.render(self.message, True, self.color_text)

            if self.x < mouse[0] < self.x + self.weight:
                if self.y < mouse[1] < self.y + self.height:
                    if click[0] == 1 and self.action is not None:

                        if self.type == "default":
                            self.action()
                        elif self.type == "level":
                            self.action(self.message)


        else:
            font_c = pygame.font.SysFont("Verdana", t)
            text_surface = font_c.render("🔒", True, self.color_text)
        pygame.draw.rect(self.scr, self.color, (self.x, self.y, self.weight, self.height))

        self.scr.blit(text_surface, (
            self.x + (self.weight - text_surface.get_width()) / 2,
            self.y + (self.height - text_surface.get_height()) / 2))
