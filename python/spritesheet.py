import pygame

class SpriteSheet:
    def __init__(self, file,
            grid_size = (5,5), # example parameters
            tile_size = (100,100),
            margin = (0,0),
            offset = (0,0)):
        self.sheet = pygame.image.load(file).convert()
        self.grid_size = grid_size # columns, rows
        self.tile_size = tile_size
        self.margin = margin
        self.offset = offset

    def get_image(self, grid_x, grid_y):
        """
        Grab a single image from this spritesheet
        
        :param grid_x: The x coordinate of the tile in the grid
        :param grid_y: The y coordinate of the tile in the grid

        :return: The image at the specified grid location
        """
        rect = (
            grid_x * (self.margin[0] + self.tile_size[0]) + self.offset[0],
            grid_y * (self.margin[1] + self.tile_size[1]) + self.offset[1],
            self.tile_size[0],
            self.tile_size[1])
        image = pygame.Surface((self.tile_size[0], self.tile_size[1]))
        image.blit(self.sheet, (0, 0), rect)
        return image
    