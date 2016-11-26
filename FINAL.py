#    15-112: Principles of Programming and Computer Science
#    Final Project: Guitar Hero 
#    Name: Buthayna AlMulla
#    AndrewID  : bmulla
#    File Created: 10th of November 2016
#    start                       end
#    10/11    12:00     10/11    14:00
#    11/11    09:00     11/11    13:03
#    12/11    19:32     12/11     00:21
#    13/11    13:54     13/11     14:57
#    13/11    19:38     13/11     00:24
#    14/11    09:37     14/11     18:12
#    16/11    13:24     16/11     17:21
#    21/11    09:30     21/11     12:03
#    22/11    13:21     22/11     14:04
#    23/11    10:30     23/11     15:09
#    24/11    13:21     24/11     17:32
#    24/11    22:49     24/11     02:30
#    25/11    13:23     26/11     03:18
####################### SOURCES #############




##########################  IMPORTS ##################

import pygame
import notes
import random
from pygame.locals import  *
import time

####################### GAMES SET UP #####################

pygame.init()
pygame.mixer.init()
clock= pygame.time.Clock()

################## ASSIGNING COLORS #############################
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



##################  DISPLAY SETTINGS ###############################
display_width = 800
display_height = 600
gameDisplay=pygame.display.set_mode((display_width,display_height)) #sets display and its size.
pygame.display.set_caption('Guitar Hero')

###################  LOADING IMAGE SOUNDS#####################
BOO_sound = pygame.mixer.Sound("Boohoo.ogg")
WOO_sound = pygame.mixer.Sound("cheer.ogg")

######################  LOADING IMAGES ####################################
S_1=pygame.image.load('sprite_01.png')
S_2=pygame.image.load('sprite_01 2.png')
S_3=pygame.image.load('sprite_01 3.png')
S_4=pygame.image.load('sprite_01 4.png')
S_5=pygame.image.load('sprite_01 5.png')
S_6=pygame.image.load('sprite_01 6.png')
SS_1=pygame.image.load('ACe_1.gif')
SS_2=pygame.image.load('ACe_2.gif')
SS_3=pygame.image.load('ACe_3.gif')
SS_4=pygame.image.load('ACe_4.gif')
SS_5=pygame.image.load('ACe_5.gif')
SS_6=pygame.image.load('ACe_6.gif')
SS_7=pygame.image.load('ACe_7.gif')
SS_8=pygame.image.load('ACe_8.gif')


######################  SCREEN FUNCTIONS###########################

def homeScreen():
    global Screen
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, mint, [100,0,600,display_height])
    font=pygame.font.SysFont(None,40)
    song1= font.render("Click 'a' to choose Right Places" , True, black)
    gameDisplay.blit(song1,(102,50))
    song2 = font.render("Click 'b' to choose Let it gooo" , True, black)
    gameDisplay.blit(song2,(102,100))
    Difficulty1= font.render("Click '1' to pick begninner " , True, black)
    gameDisplay.blit(Difficulty1,(102,150))
    Difficulty2= font.render("Click '2' to pick normal " , True, black)
    gameDisplay.blit(Difficulty2,(102,200))
    Difficulty3= font.render("Click '3' to pick hard " , True, black)
    gameDisplay.blit(Difficulty3,(102,250))
    
    instructions = font.render("Click 'i' to read instructions" , True, black)
    gameDisplay.blit(instructions,(102,350))
    
    choice = font.render("The song you chose is "+str(song) , True, black)
    gameDisplay.blit(choice,(102,400))
    Diff = font.render("The difficulty is "+str(diffSetting) , True, black)
    gameDisplay.blit(Diff,(102,450))
    play = font.render("Click Space to start game" , True, black)
    gameDisplay.blit(play,(102,500))
    EXIT= font.render("Click 'e' to exit game" , True, black)
    gameDisplay.blit(EXIT,(102,550))
    
    pygame.display.update()
    
    Screen="home"

def characterScreen():
    global Screen
    Screen="characterScreen"
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, mint, [100,0,600,display_height])
    font=pygame.font.SysFont(None,30)
    font2=pygame.font.SysFont(None,40)
    Choice = font2.render("Choose a character" , True, black)
    gameDisplay.blit(Choice,(150,50))
    Choice1 = font.render("Click 'g' for this one" , True, black)
    gameDisplay.blit(Choice1,(350,100))
    Choice2 = font.render("Click 'f' for this one" , True, black)
    gameDisplay.blit(Choice2,(100,100))
    
    Sprite_1(150,200,mint)
    Sprite_2(350,200,mint)
    play = font.render("Click 'c' to start game" , True, black)
    gameDisplay.blit(play,(102,500))
    pygame.display.update()
    
    

def instructionScreen():
    global Screen
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, mint, [100,0,600,display_height])
    font=pygame.font.SysFont(None,40)
    play = font.render("Click Space to 'b' to go back" , True, black)
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
    Screen="instructions"
    
def gameOverScreen():
    global Screen
    fonta=pygame.font.Font(None,40)
    pygame.draw.rect(gameDisplay, lwatermellon, [100,100,600,400])
    text1 = fonta.render("Game Over!" , True, black)
    gameDisplay.blit(text1,(300,100))
    text2 = fonta.render("Your score is: "+str(Score) , True, black)
    gameDisplay.blit(text2,(100,300))
    text3 = fonta.render("Click 't' to play again: " , True, black)
    gameDisplay.blit(text3,(100,350))
    text4 = fonta.render("Click 'b' to go back to home screen: " , True, black)
    gameDisplay.blit(text4,(100,400))
    text5 = fonta.render("Click 'e' to exit game " , True, black)
    gameDisplay.blit(text5,(100,450))
    pygame.display.update()
    Screen="gameOver"

    
def pauseScreen():
    global Screen
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, mint, [100,0,600,display_height])
    font=pygame.font.SysFont(None,40)
    play = font.render("Click 'r' to resume game" , True, black)
    gameDisplay.blit(play,(100,100))
    play = font.render("Click 't' to repeat game" , True, black)
    gameDisplay.blit(play,(100,200))
    text4 = font.render("Click 'b' to go back to home screen: " , True, black)
    gameDisplay.blit(text4,(100,300))
    play = font.render("Click 'e' to exit game" , True, black)
    gameDisplay.blit(play,(100,400))
    pygame.display.update()
    Screen="pause"
 
def gameScreen():
    #Drawing the screen
    global Screen
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, mint, [200,0,100,display_height])
    pygame.draw.rect(gameDisplay, dmint, [200,500,100,100])
    pygame.draw.rect(gameDisplay, blue, [300,0,100,display_height])
    pygame.draw.rect(gameDisplay, dblue, [300,500,100,100])
    pygame.draw.rect(gameDisplay, violet, [400,0,100,display_height])
    pygame.draw.rect(gameDisplay, dviolet, [400,500,100,100])
    pygame.draw.rect(gameDisplay, watermellon, [500,0,100,display_height])
    pygame.draw.rect(gameDisplay, dwatermellon, [500,500,100,100])
    ScoreLabel(Score)
    Screen="Game"

#this screen contains all the stuff that the user will want to see; Score, combo and lives
def ScoreLabel(Score):
    global lives
    pygame.draw.rect(gameDisplay, black, [0,0,100,100])
    font=pygame.font.SysFont(None,25)
    text = font.render("Score: " + str(Score), True, white)
    gameDisplay.blit(text,(0,0))
    text2 = font.render("Lives: " + str(lives), True, white)
    gameDisplay.blit(text2,(0,20))
    text3 = font.render("Combo: " + str(Combo), True, white)
    gameDisplay.blit(text3,(0,40))
    pygame.display.update()

####################   ACTION FUNCTIONS  ############################

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

def Sprite_1(x,y,bg):
    images=[S_1,S_1,S_2,S_2,S_3,S_3,S_4,S_4,S_5,S_5,S_6,S_6]
    pygame.draw.rect(gameDisplay, bg, [x,y,160,160])
    #moding by 12 would moving along the list
    gameDisplay.blit(images[Sprites%12],(x,y))

def Sprite_2(x ,y,bg):
    images_2=[SS_1,SS_2,SS_3,SS_4,SS_5,SS_6,SS_7,SS_8]
    pygame.draw.rect(gameDisplay, bg, [x,y,240,200])
    #moding by 12 would moving along the list
    gameDisplay.blit(images_2[Sprites%8],(x,y))
    
    

#This function will animate the notes and Sprite
def animateNotes():
    global speed
    global allNotes
    global Sprites
    global Character
    if Character==1:
        Sprite_1(0,100,black)
    if Character==2:
        Sprite_2(0,100,black)
    Sprites+=1
    #We only animate the notes if we have ones summoned.
    #we redraw the bars
    if len(allNotes)>0:
        pygame.draw.rect(gameDisplay, mint, [200,0,100,display_height])
        pygame.draw.rect(gameDisplay, dmint, [200,500,100,100])
        pygame.draw.rect(gameDisplay, blue, [300,0,100,display_height])
        pygame.draw.rect(gameDisplay, dblue, [300,500,100,100])
        pygame.draw.rect(gameDisplay, violet, [400,0,100,display_height])
        pygame.draw.rect(gameDisplay, dviolet, [400,500,100,100])
        pygame.draw.rect(gameDisplay, watermellon, [500,0,100,display_height])
        pygame.draw.rect(gameDisplay, dwatermellon, [500,500,100,100])
        #we draw every note summoned and places in the list
        for anote in allNotes:
            anote.moveNote(gameDisplay,display_height,speed)
        #I update at the end as it is faster that way and more efficient.
        pygame.display.update()

#This will generate random notes. There will be a placebo effect people will believe the notes are in rhythm
def randomNotes():
    global now
    global randtime
    colors=[mint, blue, violet, watermellon]
    #randtime will randomly pick how far apart the notes are
    #This will generate a note only a random time
    if time.time() >= now+randtime:
        summonNote(random.choice(colors))
        #The now will be needed to measure how much time passes between each note
        now = time.time()
        randtime=random.uniform(0.2,1)


################    INITIALISING VARIABLES    ##############################

#This is so the game will know which screen is on. helpful for pressing keys
Screen=""

#name of the song and the song file
song="None"
songFile="None"

#This now function will be used in the random notes function. So after a given time another note will be summoned
now=0

#These determine the speed of the game. tRange must be altered accrodingly with speed
speed=14
tRange=0.5
randtime=random.uniform(0,tRange)
diffSetting="Normal"

#This will contain all the notes
allNotes=[]

#gaming and score keeping
lives=3
Score=0
Combo=0

#This is used in Sprites so we pick a frame accordingly
Sprites=1
Character=0

#Loop ends when this is true
gameExit = False

#The game starts with the home screen
homeScreen()

############### MAIN LOOP START#####################################

while not gameExit:
    #gets every event that happens
    for event in pygame.event.get(): 
        if event.type ==  pygame.QUIT:#to quit game when someone clicks x
            gameExit = True
        #here will control the keys pressed. Note that I made conditions. The game knows which screen is on. Keys will work only when the appropriate screen is on.
        if event.type == pygame.KEYDOWN:
#######Screen keys
            if Screen=="home":
                # first song option
                if event.key == pygame.K_a :
                    song= "Right moves"
                    songFile="Right_moves.mp3"
                    homeScreen()
                #second song option
                if event.key == pygame.K_b:
                    song = "Let it gooo"
                    songFile="let_it_go.mp3"
                    homeScreen()
                #instruction screen
                if event.key == pygame.K_i :
                    instructionScreen()
                #This starts up the game when space is clicked. Game will only start if a song is picked
                if event.key == pygame.K_SPACE and (Screen=="home") and songFile!="None":
                    characterScreen()
                #options of difficulty
                if event.key == pygame.K_1:
                    speed=7
                    tRange=1
                    diffSetting="Beginner"
                    homeScreen()
                if event.key == pygame.K_2:
                    speed=10
                    tRange=0.2
                    diffSetting="normal"
                    homeScreen()
                if event.key == pygame.K_3:
                    speed=12
                    tRange=0.
                    diffSetting="hard"
                    homeScreen()
                #to exit
                if event.key == pygame.K_e:
                    gameExit = True
                   # pygame.quit()

######Instruction keys
            if event.key == pygame.K_b and Screen=="instructions":
                homeScreen()


####### charcter keys
            if Screen=="characterScreen":
                #starts game only if charcter is chosen
                if event.key == pygame.K_c  and Character!=0:
                    gameScreen()
                    pygame.mixer.music.load(songFile)
                    pygame.mixer.music.set_volume(1)
                    pygame.mixer.music.play(-1)#Game will loop forever until the player loses
                #two choices
                if event.key == pygame.K_f:
                    characterScreen()
                    pygame.draw.circle(gameDisplay, lwatermellon, (200,300), 100, 3)
                    pygame.display.update()
                    Character=1
                if event.key == pygame.K_g:
                    characterScreen()
                    pygame.draw.circle(gameDisplay, lwatermellon, (490,300), 100, 3)
                    pygame.display.update()
                    Character=2

########game keys
            if Screen=="Game":
                #here the game is paused
                if event.key == pygame.K_p :
                    pauseScreen()
                    pygame.mixer.music.pause()

            #Pressing keys to get the notes is here
            #when a key is pressed, the game checks each note to see if it's within the region. If it is the user gets a point. The note is removed to show that it was accounted for.
                elif event.key == pygame.K_s:
                    for anote in allNotes:
                        if anote.y>530 and anote.y<630 and anote.x==250:
                            Score+=1
                            Combo+=1
                            allNotes.remove(anote)
                            ScoreLabel(Score)
                elif event.key == pygame.K_d:
                    for anote in allNotes:
                        if anote.y>530 and anote.y<630 and anote.x==350:
                            Score+=1
                            Combo+=1
                            allNotes.remove(anote)
                            ScoreLabel(Score)
                elif event.key == pygame.K_j:
                    for anote in allNotes:
                        if anote.y>530 and anote.y<630 and anote.x==450:
                            Score+=1
                            Combo+=1
                            allNotes.remove(anote)
                            ScoreLabel(Score)
                elif event.key == pygame.K_k:
                    for anote in allNotes:
                        if anote.y>530 and anote.y<630 and anote.x==550:
                            Score+=1
                            Combo+=1
                            allNotes.remove(anote)
                            ScoreLabel(Score)

####### pause keys
            if Screen=="pause":
                #resume button
                if event.key == pygame.K_r:
                    gameScreen()
                    pygame.mixer.music.unpause()
                #this exits the game
                if event.key == pygame.K_e:
                    gameExit = True
                    pygame.quit()
                #This restarts the game
                if event.key == pygame.K_t:
                    #setting everything back to what it was
                    Score=0
                    lives=3
                    allNotes=[]
                    gameScreen()
                    ScoreLabel(Score)
                    pygame.mixer.music.play()
                #back to menu button
                if event.key == pygame.K_b:
                    pygame.mixer.music.stop()
                    pygame.mixer.stop()
                    Score=0
                    lives=3
                    allNotes=[]
                    homeScreen()

#########Game over keys
            if Screen=="gameOver":
                #rewind button
                if event.key == pygame.K_t:
                    #setting everything back to what it was
                    Score=0
                    lives=3
                    allNotes=[]
                    gameScreen()
                    ScoreLabel(Score)
                    #rewinding the song
                    pygame.mixer.music.rewind()
                    pygame.mixer.music.play()
                #exit button
                if event.key == pygame.K_e:
                    gameExit = True
                    pygame.quit()
                #back to menu button
                if event.key == pygame.K_b:
                    pygame.mixer.music.stop()
                    pygame.mixer.stop()
                    Score=0
                    lives=3
                    allNotes=[]
                    homeScreen()

##########game activity################
        
    #checking all notes to check for missed notes and to remove them. 
    for anote in allNotes:
        if anote.y>630:
            allNotes.remove(anote)
            lives=lives-1
            #note is missed Combo is back to 0
            Combo=0
            ScoreLabel(Score)
            #This will play the BOOOO sound
            WOO_sound.stop()
            BOO_sound.play()
        #The user Loses when there aren't any lives yet
        if lives==0:
            gameOverScreen()          
#This  will call the animate function only if the screen is game. This will pause the animation when the pause screen is on. 
    if Screen=="Game" and Screen!="Pause":
        randomNotes()
        animateNotes()
        #here I will check the score and after 40 points of no misses the user will get a cheer
        if (Combo+1)%40 ==1 and Combo!=0:
            WOO_sound.play()
##########################GAME LOOP END######################
pygame.quit()
            
