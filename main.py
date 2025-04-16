import pygame
import sys
import random

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

# Configuração dos canos
PIPE_DISTANCE = 100
PIPE_SPEED = 3
PIPE_HEIGHT = ground.get_height()

def create_pipes():
    base_height = random.randint(150, 300)
    y_bottom_pipe = base_height
    y_top_pipe = base_height - PIPE_DISTANCE - pipe.get_height()
    return {'x':SCREEN_WIDTH,
            'top':y_top_pipe,
            'bottom':y_bottom_pipe
            }


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
# Lista de canos
pipes = [create_pipes()]

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

        for p in pipes:
            p['x'] -= PIPE_SPEED
        # Adicionar novo cano quando necessário
        if pipes[-1]['x'] < SCREEN_WIDTH - 150:
            pipes.append(create_pipes())
        # Remover canos que não sao mais visiveis
        if pipes[0]['x'] < -pipe.get_width():
            pipes.pop(0)

        # Desenhar os elementos
        screen.blit(bg,(0,0))
        # Desenhar os canos
        for p in pipes:
            screen.blit(pipe, (p['x'], p['top']))
            flipped_pipe = pygame.transform.flip(pipe, False, True)
            screen.blit(flipped_pipe, (p['x'], p['bottom']))
        screen.blit(bird_frames[bird_index],(bird_pos_x, bird_pos_y))
        screen.blit(ground, (0,SCREEN_HEIGHT- ground.get_height()))
        pygame.display.update()
        clock.tick(FPS)
