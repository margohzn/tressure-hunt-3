import pygame 
import random
import time 
from pygame.locals import * 

screen_width = 900
screen_height = 800 


def change_background(image):
    image = pygame.image.load(image)
    bg = pygame.transform.scale(image, (screen_width, screen_height))
    screen.blit(bg, (0,0))




pygame.init()
pygame.display.set_caption("Tressure Hunt")
screen = pygame.display.set_mode([screen_width, screen_height])


#player sprite  (pirate is the player sprite)

class Pirate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pirate.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect()

#player sprite (stone is the player sprite)

class Stone(pygame.sprite.Sprite):
    def __init__(self, img_name):
        super().__init__()
        self.image = pygame.image.load(img_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()


# list of image names for stone class 
images = ["images/stone1.png", "images/stone2.png", "images/stone3.png"]

# creating spirte groups (like in flappybird with the pipes and the birds)
stone_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# creating stone sprites object
for i in range(100):
    stone = Stone(random.choice(images))
    stone.rect.x = random.randrange(screen_width)
    stone.rect.y = random.randrange(screen_height)
    # adding stone sprite to the groups
    stone_group.add(stone)
    all_sprites.add(stone)


#creat pirate sprite object
pirate = Pirate()
all_sprites.add(pirate)

playing = True 
score = 0 
WHITE = (255,255,255)
RED = (255,0,0)
clock = pygame.time.Clock()
start_time = time.time()
my_font = pygame.font.SysFont("Times New Roman", 40)
timing_font = pygame.font.SysFont("Times New Roman", 70)
text = my_font.render("Score: " +str(score), True, WHITE)



while playing:
    #screen refreshed 60 times a second by default  
    clock.tick(30) # we are changing it to be 30 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    time_elapsed = time.time() - start_time
    if time_elapsed >= 30:
        text = my_font.render("Game over", True, WHITE)
        screen.blit(text, (300,40))
    else:
        change_background("images/background.png")

        #move the pirate to collect stones 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if pirate.rect.y > 0:
                pirate.rect.y -= 5 
        if keys[pygame.K_DOWN]:
            if pirate.rect.y < 730:
                pirate.rect.y += 5 
        if keys[pygame.K_RIGHT]:
            if pirate.rect.x < 850:
                pirate.rect.x += 5
        if keys[pygame.K_LEFT]:
            if pirate.rect.x > 0:
                pirate.rect.x -= 5 
        
        stone_hit_list = pygame.sprite.spritecollide(pirate, stone_group, True)
        for stone in stone_hit_list:
            score += 1
            text = my_font.render("Score:" +str(score), True, WHITE)
        screen.blit(text, (730,80))
        all_sprites.draw(screen)

    pygame.display.update()


pygame.quit()
            



        

    




