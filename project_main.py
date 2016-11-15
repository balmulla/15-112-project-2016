#    15-112: Principles of Programming and Computer Science
#    Final Project: Guitar Hero 
#    Name      : Buthayna AlMulla
#    AndrewID  : bmulla
#    File Created: 10th of November 2016
#    start                       end
#    10/11    12:00     10/11    14:00
#    11/11    09:00     11/11    13:03
#    12/11    19:32     12/11     00:21
#    13/11    13:54     13/11     14:57
#    13/11    19:38     13/11   00:24
#    14/11    09:37      
########## sources #############




########## Imports###########

import pygame
import notes
import random
from pygame.locals import  *
#import time




######### Game Set Up #########

pygame.init()
clock= pygame.time.Clock()
#clock= pygame.time.Clock() #setting the time

# assigning colors
black=(0,0,0)
white=(255,255,255)
lmint=(41, 81, 66)
mint=(112,249,174)
dmint=(60, 168, 109)
blue=(67,134,242)
dblue=(45, 92, 163)
lblue=(177, 205, 249)
violet=(249,112,236)
dviolet=(138, 50, 140)
lviolet=(238, 201, 252)
watermellon=(249,112,137)
dwatermellon=(186, 94, 125)
lwatermellon=(252, 201, 212)

display_width = 800
display_height = 600


#setting the display
gameDisplay=pygame.display.set_mode((display_width,display_height)) #sets display and its size.
pygame.display.set_caption('Guitar Hero')

def homeScreen():
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, mint, [100,0,600,display_height])
    font=pygame.font.SysFont(None,40)
    song1= font.render("Click 'a' to choose bulletproof heart" , True, black)
    gameDisplay.blit(song1,(102,50))
    song2 = font.render("Click 'b' to choose mama" , True, black)
    gameDisplay.blit(song2,(102,100))
    choice = font.render("The song you chose is "+str(song) , True, black)
    gameDisplay.blit(choice,(102,200))
    play = font.render("Click Space to start game" , True, black)
    gameDisplay.blit(play,(102,300))
    instructions = font.render("Click 'i' to read instructions" , True, black)
    gameDisplay.blit(instructions,(102,400))
    pygame.display.update()

def instructionScreen():
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, mint, [100,0,600,display_height])
    font=pygame.font.SysFont(None,40)
    play = font.render("Click Space to start game" , True, black)
    gameDisplay.blit(play,(100,100))
    instructions1 = font.render("Notes will come down." , True, black)
    gameDisplay.blit(instructions1,(100,150))
    instructions2 = font.render("You must press 's' if the note is Lime." , True, black)
    gameDisplay.blit(instructions2,(100,200))
    instructions3 = font.render("You must press 'd' if note is blue." , True, black)
    gameDisplay.blit(instructions3,(100,250))
    instructions4 = font.render("You must press 'j' if note is violet" , True, black)
    gameDisplay.blit(instructions4,(100,300))
    instructions5 = font.render("You must press 'k' if note is dusty rose" , True, black)
    gameDisplay.blit(instructions5,(100,350))
    instructions6 = font.render("Press 'p' to pause game. " , True, black)
    gameDisplay.blit(instructions6,(100,400))
    pygame.display.update()  

def pauseScreen():
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, mint, [100,0,600,display_height])
    font=pygame.font.SysFont(None,40)
    play = font.render("Click 'r' to resume game" , True, black)
    gameDisplay.blit(play,(100,100))
    play = font.render("Click 't' to repeat game" , True, black)
    gameDisplay.blit(play,(100,200))
    play = font.render("Click 'e' to exit game" , True, black)
    gameDisplay.blit(play,(100,300))
    pygame.display.update()  
 
def gameScreen():
    #Drawing the screen
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, mint, [200,0,100,display_height])
    pygame.draw.rect(gameDisplay, dmint, [200,500,100,100])
    pygame.draw.rect(gameDisplay, blue, [300,0,100,display_height])
    pygame.draw.rect(gameDisplay, dblue, [300,500,100,100])
    pygame.draw.rect(gameDisplay, violet, [400,0,100,display_height])
    pygame.draw.rect(gameDisplay, dviolet, [400,500,100,100])
    pygame.draw.rect(gameDisplay, watermellon, [500,0,100,display_height])
    pygame.draw.rect(gameDisplay, dwatermellon, [500,500,100,100])




def ScoreLabel(Score):
    pygame.draw.rect(gameDisplay, black, [0,0,100,100])
    font=pygame.font.SysFont(None,25)
    text = font.render("Score: " + str(Score), True, white)
    gameDisplay.blit(text,(0,0))
    pygame.display.update()

allNotes=[]
speed=7
Score=0

#This function will summon the note
def summonNote(color):
    global allNotes
    if color==mint:
        anote = notes.Notes(mint,dmint,lmint,250,-60)
    elif color==blue:
        anote = notes.Notes(blue,dblue,lblue,350,-60)
    elif color==violet:
        anote = notes.Notes(violet,dviolet,lviolet,450,-60)
    elif color==watermellon:
        anote = notes.Notes(watermellon,dwatermellon,lwatermellon,550,-60)
    allNotes.append(anote)

def animateNotes():
    global allNotes
    #print "in animate"
    #resetting the screen
    pygame.draw.rect(gameDisplay, mint, [200,0,100,display_height])
    pygame.draw.rect(gameDisplay, dmint, [200,500,100,100])
    pygame.draw.rect(gameDisplay, blue, [300,0,100,display_height])
    pygame.draw.rect(gameDisplay, dblue, [300,500,100,100])
    pygame.draw.rect(gameDisplay, violet, [400,0,100,display_height])
    pygame.draw.rect(gameDisplay, dviolet, [400,500,100,100])
    pygame.draw.rect(gameDisplay, watermellon, [500,0,100,display_height])
    pygame.draw.rect(gameDisplay, dwatermellon, [500,500,100,100])
    for anote in allNotes:
        #print anote.y
        anote.moveNote(gameDisplay,display_height,speed)
        if anote.y>=660:
            pygame.time.set_timer(pygame.USEREVENT+1,0)
    #I update at the end as it is faster that way and more efficient.
    pygame.display.update()


def randomNotes():
    colors=[mint, blue, violet, watermellon]
    color=random.choice(colors)
    summonNote(color)
    pygame.time.set_timer(pygame.USEREVENT+2,0)
    
Screen="home"
song="None"
songFile="None"

#homeScreen()

gameScreen()
#ScoreLabel(Score)
#randomNotes()
summonNote(blue)
summonNote(mint)
#animateNotes()


gameExit = False

pygame.time.set_timer(pygame.USEREVENT+1,20)
#pygame.time.set_timer(pygame.USEREVENT+2,20)

#main loop
while not gameExit:
    for event in pygame.event.get(): #gets every event that happens
        if event.type ==  pygame.QUIT:#to quit game when someone clicks x
            gameExit = True
        if event.type == pygame.KEYDOWN:
            #This key is clicked on
            if event.key == pygame.K_a and Screen=="home":
                song = "Bulletproof Heart"
                songFile="03. Bulletproof Heart.mp3"
                homeScreen()
            if event.key == pygame.K_b and Screen=="home":
                song = "mama"
                songFile="10. S.C.A.R.E.C.R.O.W..mp3"
                homeScreen()
            if event.key == pygame.K_i and Screen=="home":
                instructionScreen()
                Screen="instructions"
            if event.key == pygame.K_SPACE and (Screen=="home" or Screen=="instructions") and songFile!="None":
                gameScreen()
                ScoreLabel(Score)
                Screen="Game"
                #songFile=  "03. Bulletproof Heart.mp3"    
                pygame.display.update()
                pygame.mixer.music.load(songFile)
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play()
                
            if event.key == pygame.K_p and Screen=="Game":
                pauseScreen()
                pygame.mixer.music.pause()
                Screen="pause"
            if event.key == pygame.K_r and Screen=="pause":
                gameScreen()
                ScoreLabel(Score)
                Screen="Game"
                pygame.mixer.music.unpause()
            if event.key == pygame.K_e and Screen=="pause":
                gameExit = True
                pygame.quit
                quit()
            if event.key == pygame.K_t and Screen=="pause":
                gameScreen()
                ScoreLabel(Score)
                Screen="Game"
                pygame.mixer.music.rewind()
                pygame.mixer.music.play()
            if event.key == pygame.K_s:
                for anote in allNotes:
                    if anote.y>530 and anote.y<630 and anote.x==250:
                        Score+=1
                        ScoreLabel(Score)
            if event.key == pygame.K_d:
                for anote in allNotes:
                    if anote.y>530 and anote.y<630 and anote.x==350:
                        Score+=1
                        ScoreLabel(Score)
            if event.key == pygame.K_j:
                for anote in allNotes:
                    if anote.y>530 and anote.y<630 and anote.x==450:
                        Score+=1
                        ScoreLabel(Score)
            if event.key == pygame.K_k:
                for anote in allNotes:
                    if anote.y>530 and anote.y<630 and anote.x==550:
                        Score+=1
                        ScoreLabel(Score)
    for evt in pygame.event.get():
        if evt.type==USEREVENT+1:
            if len(allNotes)!=0:
                animateNotes()
##        if evt.type==USEREVENT+2:
##            randomNotes()
        


pygame.quit
quit() 

