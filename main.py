import pygame
import sys

pygame.init()
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
FPS = 60

# Desenhar a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")
clock = pygame.time.Clock()
# Carregar os sprites
bg = pygame.image.load("assets/background-day.png").convert()
ground = pygame.image.load("assets/base.png").convert()
pipe  = pygame.image.load("assets/pipe-green.png").convert_alpha()

# Sprites dos passaros
bird_down = pygame.image.load("assets/yellowbird-downflap.png").convert_alpha()
bird_mid = pygame.image.load("assets/yellowbird-midflap.png").convert_alpha()
bird_up = pygame.image.load("assets/yellowbird-upflap.png").convert_alpha()
bird_frames = [bird_down, bird_mid, bird_up]

# Variaveis do Pássaro
bird_index = 0
bird_pos_x = 50
bird_pos_y = 256
speed = 0 # velocidade do passaro
gravity = 0.5 # gravidade
jump = 8 # Força do pulo do passaro

# Game loop
while True:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_SPACE:
                speed  = - jump
        # Aplicar gravidade
        speed += gravity
        bird_pos_y += speed

        # Atualizar os frames da animação do passaro
        bird_index = (bird_index +1) % len(bird_frames)

        # Desenhar os elementos
        screen.blit(bg,(0,0))
        screen.blit(bird_frames[bird_index],(bird_pos_x, bird_pos_y))
        screen.blit(ground, (0,SCREEN_HEIGHT- ground.get_height()))
        pygame.display.update()
        clock.tick(FPS)
