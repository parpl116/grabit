import pygame
import random
import time
import datetime
import os
# os.system("grabit.py")
with open("grabit_opt.txt", "r") as folder:
    f_list = folder.readlines()
    # print(f_list)
f_list[0] = f_list[0].replace('\n', '')
if "\n" in f_list[1]:
    f_list[1] = f_list[1].replace('\n', '')
# print(f_list)
pygame.init()
distance = 5
fps = 60
score=0
lives=3
enemy1_random1 = random.randint(60, 240)
enemy1_texture=0
enemy1_move=0
enemy2_movex=3
enemy2_movey=3
enemy4_random1 = random.randint(500, 700)
enemy4_move=0
clock = pygame.time.Clock()
width = 1000
height = 500
score_range=1
spawn_rubble=4
screen = pygame.display.set_mode((width, height))
# PLAYER
player = pygame.image.load("img/you1-front.png")
r_player = player.get_rect()
r_player.center = (random.randint(30, width)-15, random.randint(30, height)-15)
# JABLKO
apple = pygame.image.load("img/apple.png")
r_apple = apple.get_rect()
r_apple.center = (random.randint(30, width)-15, random.randint(30, height)-15)
# DIAMANT
rubble = pygame.image.load("img/rubble.png")
r_rubble = rubble.get_rect()
r_rubble.center = (width+10, height+10)
# ŽIVOTY
heart = pygame.image.load("img/heart-icon.png")
r_heart = heart.get_rect()
r_heart.topleft = (0, 0)
heart2 = pygame.image.load("img/heart-icon.png")
r_heart2 = heart2.get_rect()
r_heart2.topleft = (0+25, 0)
heart3 = pygame.image.load("img/heart-icon.png")
r_heart3 = heart3.get_rect()
r_heart3.topleft = (0+25+25, 0)
# ENEMY Grake
enemy = pygame.image.load("img/enemy1-front1.png")
r_enemy = enemy.get_rect()
r_enemy.center = (random.randint(30, width)-15, random.randint(30, height)-15)
# ENEMY DvD
enemy2 = pygame.image.load("img/you1-front.png")
r_enemy2 = enemy2.get_rect()
r_enemy2.center = (random.randint(30, height)-15, random.randint(30, height)-15)
# ENEMY SuSarah
enemy3 = pygame.image.load("img/enemy3.png")
r_enemy3 = enemy3.get_rect()
r_enemy3.center = (random.randint(30, height)-15, random.randint(30, height)-15)
# ENEMY KFC Rush
enemy4 = pygame.image.load("img/enemy4.png")
r_enemy4 = enemy4.get_rect()
r_enemy4.center = (width+35, random.randint(30, height)-15)
# SCORE
stext = pygame.font.SysFont("arial", 30)
ren_stext = stext.render("score:"+str(score), True, (255, 255, 255))
r_stext = ren_stext.get_rect()
r_stext.topright = (width, 0)
# HUDBA:
# POZADÍ
pygame.mixer.music.load("media/kupta---blue-fields.mp3")
pygame.mixer.music.play(-1)
# SEBRÁNÍ JABLKA
pick_apple = pygame.mixer.Sound("media/pick_up1.wav")
# DOTKNUTÍ SE NEPŘÍTELE
touch_enemy = pygame.mixer.Sound("media/chirp4.wav")
# DOTKNUTÍ SE NEPŘÍTELE 2
touch_enemy2 = pygame.mixer.Sound("media/hitenemy3.wav")
# NARAZENÍ DO AUTA
crash_enemy4 = pygame.mixer.Sound("media/car_window_crash.wav")
crash_enemy4.set_volume(3)
# VOLAN AUTA
horn_enemy4 = pygame.mixer.Sound("media/car_horn1.wav")
# HLAVNÍ CYKLUS
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type==256:
            lets_continue = False
    # pohyb PLAYEREM
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and r_player.top > 0:
        r_player.y -= distance
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and r_player.bottom < height:
        r_player.y += distance
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and r_player.left > 0:
        r_player.x -= distance
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and r_player.right < width:
        r_player.x += distance
    # dotek jablka
    if r_player.colliderect(r_apple):
        pick_apple.play()
        r_apple.center = (random.randint(60, width)-30, random.randint(60, height)-30)
        score+=score_range
    # dotek diamantu
    if r_player.colliderect(r_rubble):
        pick_apple.play()
        r_rubble.center = (random.randint(60, width)-30, random.randint(60, height)-30)
        score+=2
    # neprocházení přes životy
    if r_player.colliderect(r_heart) or r_player.colliderect(r_heart2) or r_player.colliderect(r_heart3):
        r_player.x+=distance
        r_player.y+=distance
    # dotek Greka
    if r_player.colliderect(r_enemy):
        touch_enemy.play()
        r_enemy.center = (random.randint(30, width)-15, random.randint(30, height)-15)
        lives-=1
    # Grakův pohyb (teleportování)
    if enemy1_move==enemy1_random1:
        r_enemy.center = (random.randint(30, width)-15, random.randint(30, height)-15)
        enemy1_move=0
        enemy1_random1 = random.randint(60, 240)
    # přeměna textur u Greka
    if enemy1_texture==40:
        enemy = pygame.image.load("img/enemy1-front2.png")
    if enemy1_texture==60:
        enemy = pygame.image.load("img/enemy1-front1.png")
    if enemy1_texture==100:
        enemy = pygame.image.load("img/enemy1-front4.png")
    if enemy1_texture==128:
        enemy = pygame.image.load("img/enemy1-front3.png")
    if enemy1_texture==150:
        enemy = pygame.image.load("img/enemy1-front2.png")
    if enemy1_texture==170:
        enemy = pygame.image.load("img/enemy1-front3.png")
        enemy1_texture=0 
    # dotek DvDho
    if r_player.colliderect(r_enemy2):
        touch_enemy.play()
        r_enemy2.center = (random.randint(30, width)-15, random.randint(30, height)-15)
        lives-=1
    # pohyb DvDho
    r_enemy2.x += enemy2_movex
    r_enemy2.y += enemy2_movey
    if r_enemy2.bottom > height:
        enemy2_movey=-3
    if r_enemy2.top < 0:
        enemy2_movey=+3
    if r_enemy2.right > width:
        enemy2_movex=-3
    if r_enemy2.left < 0:
        enemy2_movex=+3
    # dotek SuSarahy
    if r_player.colliderect(r_enemy3):
        touch_enemy2.play()
        r_enemy3.center = (random.randint(30, width)-15, random.randint(30, height)-15)
        lives-=1
    if r_enemy3.colliderect(r_enemy2):
        r_enemy3.center = (random.randint(30, width)-15, random.randint(30, height)-15)
        lives+=1
    # pohyby SuSarahy
    if r_enemy3.centerx<r_player.centerx:
        r_enemy3.centerx += 1.5
    if r_enemy3.centerx>r_player.centerx:
        r_enemy3.centerx -= 1.5
    if r_enemy3.centery<r_player.centery:
        r_enemy3.centery += 1.5
    if r_enemy3.centery>r_player.centery:
        r_enemy3.centery -= 1.5
    # pohyb a menění textur u Graka
    enemy1_move+=1
    enemy1_texture+=1
    # pohyb KFC Rushe
    enemy4_move+=1
    if enemy4_move==enemy4_random1:
        horn_enemy4.play()
    if (enemy4_move+30)==enemy4_random1:
        horn_enemy4.play()
    if enemy4_move>=enemy4_random1:
        r_enemy4.centerx -= 8
    if r_enemy4.centerx<-30:
        enemy4_move=0
        r_enemy4.center = (width+35, random.randint(30, height)-15)
        enemy4_random1=random.randint(180, 400)
    if r_player.colliderect(r_enemy4):
        crash_enemy4.play()
        lives-=2
        enemy4_move=0
        r_enemy4.center = (width+35, random.randint(30, height)-15)
        
    # opakovaný render textu ukazující skóre
    ren_stext = stext.render("score:"+str(score), True, (255, 255, 255))
    r_stext = ren_stext.get_rect()
    r_stext.topright = (width, 0)
    # blitnutí obrazovky
    screen.fill((0, 0, 0))
    # blitnutí playera
    screen.blit(player, r_player)
    # blitnutí jablka
    screen.blit(apple, r_apple)
    # blitnutí diamantu
    screen.blit(rubble, r_rubble)
    # blitnutí Graka
    screen.blit(enemy, r_enemy)
    # blitnutí DvDho
    screen.blit(enemy2, r_enemy2)
    # blitnutí SusSarahy 
    screen.blit(enemy3, r_enemy3)
    # blitnutí textu ukazující skóre
    screen.blit(ren_stext, r_stext)
    # blitnutí KFC Rushe
    screen.blit(enemy4, r_enemy4)
    # odčítání životů
    if lives>=3:
        screen.blit(heart3, r_heart3)
    if lives>=2:
        screen.blit(heart2, r_heart2)
    if lives>=1:
        screen.blit(heart, r_heart)
    # konec hry
    if lives==0:
        lets_continue=False
    # vykreslování obrazovky
    pygame.display.update()
    # fps
    clock.tick(fps)
pygame.quit()
# print(score)

if score>int(f_list[0]):
    f_list[0]=str(score)
f_list[0]+='\n'
f_list[1]=str(score)

date_in = datetime.datetime.now()
final_date = date_in.strftime(" - %d/%m/%Y %X")

with open('grabit_opt.txt', 'w') as folder:
    for i in f_list:
        folder.write(i)

with open("grabit_allscores.txt", "r") as folder:
    f_list = folder.readlines()
if len(f_list)!=1:
    f_list[len(f_list)-1] += "\n"
else:
    f_list[0]+='\n'
f_list.append(str(score) + str(final_date))
with open("grabit_allscores.txt", "w") as folder:
    for i in f_list:
        folder.write(str(i))
# print(final_date)
os.system("menu_grabit.py")