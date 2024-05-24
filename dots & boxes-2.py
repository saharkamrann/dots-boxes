import pygame

screen = width , height = 300 , 300
cellsize = 20
padding = 20
rows = cols = (width -4 * padding) // cellsize
print(rows , cols)


pygame.init()
win = pygame.display.set_mode(screen)
white = (255 , 255 , 255)
red = (252 , 91 , 122)
blue = (78 , 198 , 246)
green = (0 , 255 , 0)
black = (12 , 12 , 12)

pos = None

running = True
while running :
    win.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for r in range(rows + 1):
        for c in range(cols + 1):
            pygame.draw.circle(win , white , (c * cellsize + 2 * padding , r * cellsize + 3 * padding), 2)

    pygame.display.update()
pygame.quit()            

