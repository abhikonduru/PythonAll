import pygame
import random
pygame.init()
DIS_HEIGHT = 720
DIS_WIDTH = 1280
recHeight = int(DIS_HEIGHT*0.05)
recWidth = int(DIS_WIDTH*0.1)
screen = pygame.display.set_mode([DIS_WIDTH,DIS_HEIGHT])
pygame.display.set_caption("Dog Pet Simulator")

clock = pygame.time.Clock()
count = 0

backgroundimg = pygame.image.load('setting.png')
#backgroundimg = pygame.image.load("..\final_background.png")
background_rect = backgroundimg.get_rect(topleft=(0,0))

bed = pygame.image.load("couch.png")
bed = pygame.transform.scale(bed, (300,300))
bed_rect = bed.get_rect(topleft=(950,recHeight*10))

bed2 = pygame.image.load('couch2.png')
bed2 = pygame.transform.scale(bed2, (200,200))
bed_rect2 = bed2.get_rect(topleft=(500,recHeight*9.3))

bowl = pygame.image.load('dog_bowl.png')
bowl = pygame.transform.scale(bowl, (115,115))
bowl_rect = bowl.get_rect(topleft=(0,recHeight*14))

bowl2 = pygame.image.load('yum2.png')
bowl2 = pygame.transform.scale(bowl2, (200,200))
bowl_rect2 = bowl2.get_rect(topleft=(500,recHeight*9.8))

water = pygame.image.load('water_bowl.png')
water = pygame.transform.scale(water, (150,150))
water_rect = water.get_rect(topleft=(115,recHeight*14))

water2 = pygame.image.load('water2.png')
water2 = pygame.transform.scale(water2, (200,200))
water_rect2 = water2.get_rect(topleft=(500,recHeight*9))

corgi = pygame.image.load('corgi.png')
corgi = pygame.transform.scale(corgi, (200,200))
corgi_rect = corgi.get_rect(topleft=(650,recHeight*12))

sun = pygame.image.load('sun.png')
sun = pygame.transform.scale(sun, (150,150))
sun_rect = sun.get_rect(topleft=(825,recHeight*4.3))

moon = pygame.image.load('moon.png')
moon = pygame.transform.scale(moon, (150,150))
moon_rect = moon.get_rect(topleft=(825,recHeight*4.3))

def Need(random_num):
    if random_num == 1: #sleepy
        screen.blit(bed2,bed_rect2)  
    elif random_num ==2: #water
        screen.blit(water2,water_rect2)
    elif random_num == 3: #hungry
        screen.blit(bowl2,bowl_rect2)
keep_going = True
mouse_down = False
random_num = random.randint(1,3) 
day_or_night = random.randint(1,2)
while keep_going:
    if count>=120*5:
        if day_or_night == 1:
            day_or_night=2
        else:
            day_or_night=1
        count=0
    if day_or_night == 1:
        screen.fill((135,206,235))
        screen.blit(sun,sun_rect)
    elif day_or_night == 2:
        screen.fill((0,0,0))
        screen.blit(moon,moon_rect)
    screen.blit(backgroundimg,background_rect)  
    screen.blit(bowl,bowl_rect)
    screen.blit(water, water_rect)
    screen.blit(corgi,corgi_rect)
    screen.blit(bed,bed_rect)
    Need(random_num)
    
    for event in pygame.event.get():
        spot=pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
                keep_going = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            spot=pygame.mouse.get_pos()
            if random_num==1 and bed_rect.collidepoint(spot):
                 random_num = random.randint(2,3)
            elif random_num==2 and water_rect.collidepoint(spot):
                 t = [1,3]#numbers that I want it to generate, since I dont want the need to repeat
                 random_num = random.randint(0,1)
                 random_num = t[random_num]
            elif random_num==3 and bowl_rect.collidepoint(spot):
                 random_num = random.randint(1,2)
    clock.tick(120)
    count+=1
    pygame.display.update()
    
         