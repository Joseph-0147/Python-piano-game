import pygame
from pygame.locals import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define piano key sizes
KEY_WIDTH = 50
KEY_HEIGHT = 200

# Define key positions
KEY_POS = [(50*i, 0) for i in range(10)]

# Define key mappings to keyboard keys
KEY_MAPPING = {
    K_a: 0,
    K_s: 1,
    K_d: 2,
    K_f: 3,
    K_g: 4,
    K_h: 5,
    K_j: 6,
    K_k: 7,
    K_l: 8,
    K_SEMICOLON: 9
}

# Initialize Pygame
pygame.init()

# Load sound files for each note
sound_files = ["C.wav", "D.wav", "E.wav", "F.wav", "G.wav", "A.wav", "B.wav", "C_high.wav", "D_high.wav", "E_high.wav"]
sounds = [pygame.mixer.Sound(sound_file) for sound_file in sound_files]

# Set the dimensions of the window
WINDOW_SIZE = (KEY_WIDTH * 10, KEY_HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Virtual Piano")

# Create clock object to control refresh speed
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Check if the pressed key corresponds to a piano key
            if event.key in KEY_MAPPING:
                key_index = KEY_MAPPING[event.key]
                key_rect = pygame.Rect(KEY_POS[key_index], (KEY_WIDTH, KEY_HEIGHT))
                pygame.draw.rect(screen, RED, key_rect)
                # Play the corresponding sound
                sounds[key_index].play()

    # Get currently pressed keys
    keys = pygame.key.get_pressed()

    # Check for released keys
    for key, index in KEY_MAPPING.items():
        if not keys[key]:
            key_rect = pygame.Rect(KEY_POS[index], (KEY_WIDTH, KEY_HEIGHT))
            pygame.draw.rect(screen, WHITE, key_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
