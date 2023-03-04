import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Creating display surface
window_width = 800
window_height = 800
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Chess")

# Creating the Chessboard
class BoardSquare:
    def __init__(self, pixel_x, pixel_y, tile_size, is_white):
        self.pixel_x = pixel_x
        self.pixel_y = pixel_y
        self.tile_size = tile_size
        self.is_white = is_white

def calculate_coordinates(x_array, y_array, is_white):
    if window_width < window_height or window_height == window_height:
        tile_size = window_width / 8
    else: 
        tile_size = window_height / 8
    
    pixel_x = x_array * tile_size
    pixel_y = y_array * tile_size

    return BoardSquare(pixel_x, pixel_y, tile_size, is_white)


chess_board = []
for y in range(8):
    chess_row = []
    for x in range(8): 
        x_even = x % 2 == 0
        y_even = y % 2 == 0  
        is_white = x_even == y_even
        chess_row.append(calculate_coordinates(x,y, is_white))
    
    chess_board.append(chess_row)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for row in chess_board:
        for square in row:
            surf = pygame.Surface((square.tile_size, square.tile_size))
            if square.is_white:
                surf.fill((255,255,255))
            else:
                surf.fill((0,0,0))        
            rect = surf.get_rect()
            screen.blit(surf, (square.pixel_x, square.pixel_y))

    pygame.display.flip()
    clock.tick(60)