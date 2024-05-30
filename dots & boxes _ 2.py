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

class cell:
    def __init__(self,r,c):
        self.r = r
        self.c = c
        self.index = self.r * rows 


pos = None

running = True
while running :
    win.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type  == pygame.MOUSEBUTTONDOWN:
            pos = event.pos


    for r in range(rows + 1):
        for c in range(cols + 1):
            pygame.draw.circle(win , black , (c * cellsize + 2 * padding , r * cellsize + 3 * padding), 2)

    if pos:
        pygame.draw.circle(win , red ,pos , 2)

    pygame.display.update()
pygame.quit()            

