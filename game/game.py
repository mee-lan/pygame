import pygame
from sys import exit
pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #Main display surface over which we draw other (regular)surfaces
pygame.display.set_caption("Traffic") # gives name to the window
clock = pygame.time.Clock() #needed to manage FPS
test_font = pygame.font.Font('py_game/fonts/small_pixel.ttf',50) #font type and font size params

#STATE:
game_active = True


#SURFACES:
sky_surface = pygame.image.load('py_game/graphics/sky.png').convert()
bot_surface = pygame.image.load('py_game/graphics/bot.png').convert_alpha()
ground_surface = pygame.image.load('py_game/graphics/groundimg.jpg').convert()
text_surface = test_font.render('SCORE: 69',False,(64,64,64)) #text, antiAlias, color
player_surface = pygame.image.load('py_game/graphics/player1.png').convert_alpha()



#Transform images
sky_surface= pygame.transform.scale(sky_surface,(SCREEN_WIDTH,SCREEN_HEIGHT*0.8))
ground_surface= pygame.transform.scale(ground_surface,(SCREEN_WIDTH,SCREEN_HEIGHT*0.2))
bot_surface = pygame.transform.scale(bot_surface,(100,100))
player_surface = pygame.transform.scale(player_surface,(300,250))

#RECTANGLE:
# converting surface to rect allows to take difference anchor points of image to place
player_rect = player_surface.get_rect(midbottom = (100,SCREEN_HEIGHT*0.85))
bot_rect = bot_surface.get_rect(midbottom = (SCREEN_WIDTH,SCREEN_HEIGHT*0.8))
text_rect = text_surface.get_rect(center = (SCREEN_WIDTH//2,50))
# use midbottom, midleft, topleft,center etc

player_gravity =0

c=0
while True:

    if game_active: #state representing user is playing the game
        screen.blit(ground_surface,(0,SCREEN_HEIGHT*0.8))
        screen.blit(sky_surface,(0,0)) #blit = block image transfer (used to diplay surfaces )
        pygame.draw.rect(screen,'#c0e8a6',text_rect,10,border_radius=5) 
        pygame.draw.rect(screen,'#c0e8a6',text_rect)
        screen.blit(text_surface,text_rect)
        screen.blit(bot_surface,bot_rect)
        screen.blit(player_surface,player_rect)

                
        player_rect.left+=1 #move player to right

        player_rect.bottom+=player_gravity
        player_gravity+=0.1
        print(player_rect.bottom)
        if player_rect.bottom>=SCREEN_HEIGHT*0.85: player_rect.bottom = SCREEN_HEIGHT*0.85

        
        #if doesnot collide move bot to the left else
        if(not player_rect.colliderect(bot_rect)):
            if (bot_rect.right>-100): bot_rect.right-=5
            else: bot_rect.right=SCREEN_WIDTH
        else:
             print("collission")
             game_active=False

    else:
        screen.fill('Yellow')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                player_gravity=-5
        
        if event.type == pygame.KEYDOWN:
            #print("key up")
            if event.key ==  pygame.K_SPACE:
                if(player_rect.bottom>=SCREEN_HEIGHT*0.85):
                    print(player_rect.bottom)
                    print(player_gravity)
                    player_gravity=-8

    

    pygame.display.update()
    clock.tick(144) # sets the FPS to 60fps

 