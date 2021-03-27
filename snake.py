import pygame
import time
import random


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('gloria-tells-tell-me-now.mp3')
pygame.mixer.music.play(10)

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Ehkater')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

font_style2 = pygame.font.SysFont("bahnschrift", 55)
white = (1, 37, 40)
display_surface = pygame.display.set_mode((dis_width, dis_height))

bg = pygame.image.load("sky.jpg")

image = pygame.image.load('ship.jpg')

def game_intro():
     intro = True

     while intro == True:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop()
        dis.fill(white)
        message3(" Pixel Snake ", red)
        display_surface.blit(image, (100, 100))
        message2(" To Start press c ", red)

        pygame.display.update()
        clock.tick(15)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

    
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
     
     
     
