import pygame


class Color:
    def __init__(self, col):
        self.col = col

    def interpColors(self, col2, t):
        if len(self.col) == 3 or len(col2) == 3:
            return self.col[0] * t + col2[0] * (1 - t), self.col[1] * t + col2[1] * (1 - t), self.col[2] * t + col2[
                2] * (1 - t)
        else:
            return self.col[0] * t + col2[0] * (1 - t), self.col[1] * t + col2[1] * (1 - t), self.col[2] * t + col2[
                2] * (1 - t), self.col[3] * t + col2[
                       3] * (1 - t)

    def draw_polygon_alpha(surface, c, ps):
        x, y = zip(*ps)
        min_x, min_y, max_x, max_y = min(x), min(y), max(x), max(y)
        newRect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
        surf = pygame.Surface(newRect.size, pygame.SRCALPHA)
        pygame.draw.polygon(surf, c, [(i - min_x, j - min_y) for i, j in ps])
        surface.blit(surf, newRect)

    def draw_circle_alpha(surface, c, center, r, length):
        newRect = pygame.Rect(center, (0, 0)).inflate((r * 2, r * 2))
        surf = pygame.Surface(newRect.size, pygame.SRCALPHA)
        pygame.draw.circle(surf, c, (r, r), r, length)
        surface.blit(surf, newRect)

    def draw_rect_alpha(surface, c, rect):
        surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(surf, c, surf.get_rect())
        surface.blit(surf, rect)
