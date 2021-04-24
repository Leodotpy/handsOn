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

    # TODO: CHANGE THIS
    def draw_polygon_alpha(surface, color, points):
        lx, ly = zip(*points)
        min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
        target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
        surface.blit(shape_surf, target_rect)