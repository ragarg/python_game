import sys, pygame
import Core

pygame.init()

size = width, height = 900, 600
screen = pygame.display.set_mode(size)
core = Core.Core()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                core.update_way(mouse_pos)

    cells = core.update_field()

    for line in cells:
        for obj in line:
            if not obj[0] is None:
                screen.blit(obj[0].image, (obj[0].x * 24, obj[0].y * 24))
            if not obj[1] is None:
                screen.blit(obj[1].image, (obj[1].x * 24, obj[1].y * 24))

    pygame.time.wait(100)
    pygame.display.flip()
