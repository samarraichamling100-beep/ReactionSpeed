import pygame, random

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

X_POS = 100
Y_POS = 100

def randomize_pos():
    global X_POS, Y_POS

    X_POS = random.randint(30, 770)
    Y_POS = random.randint(30, 770)

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    MousePos = pygame.mouse.get_pos()

    CircleCollision = pygame.Rect(X_POS - 30, Y_POS - 30, 60, 60)

    if CircleCollision.collidepoint(MousePos):
        randomize_pos()

    screen.fill((20, 20, 20))
    pygame.draw.circle(screen, (100, 20, 20), (X_POS, Y_POS), 30)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()