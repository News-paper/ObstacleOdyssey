import pygame 

pygame.init()
screen = pygame.display.set_mode((700,700))

clock=pygame.time.Clock()
running= True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
colourTup=(255,0,0)
coordinatesTup=(50,50)
            
pygame.draw.circle(screen,colourTup,coordinatesTup,50,width=0)
            
      
screen =[1,3,4,5,6,7,8]
      
playerpos=3 
screen[playerpos]=8
print(screen)
background_colour=(93,84,83)
screen.fill(background_colour)

pygame.display.flip()
clock.tick(60)#setting the fps to 60

pygame.quit()
        
