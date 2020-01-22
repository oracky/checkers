class Settings:
    screen_width = 1100
    screen_height = 640
    background_color = (220, 220, 220)
    color1 = (255, 255, 255)                     # white
    color2 = (0, 0, 0)                           # black
    player1_color = (255, 0, 0)                  # red
    player2_color = (0, 0, 255)                  # blue
    move_color = (153, 77, 0)                    # brown
    tile_width = int(screen_height/8)
    tile_height = int(screen_height/8)
    piece_center = (int(tile_width/2), int(tile_height/2))
    piece_radius = int(tile_height/2 - 0.1*tile_height)
