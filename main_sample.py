import sys, pygame
import Core

pygame.init()
print("hi")

size = width, height = 1440, 1440
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
                core.Hero.ActiveIndicator = 1             
    
    for line in core.loc.field:
        for obj in line:
            if not obj is None:
                screen.blit(obj.image, (obj.x, obj.y * 24))
    
    pygame.display.flip()
