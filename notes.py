import pygame
#I want to generate a function that generates notes when functions are called
class Notes():
    def __init__(self, color,dcolor,lcolor,x,y):
#the color can be mint, blur, violet or watermellon
        self.color=color
        self.dcolor=dcolor
        self.lcolor=lcolor
        self.x=x
        self.y=y
        #This function will need to know where to generate the note, mint 250, blue 350, violet 450, watermellon 550.
    def __str__(self):
        results=str(self.color)+":"+str(self.dcolor)+":"+str(self.lcolor)+":"+str(self.x)+":"+str(self.y)
        return results
    def generateNote(self,gameDisplay): #Takes the height of the window
        pygame.draw.circle(gameDisplay, self.lcolor, (self.x,self.y), 30, 3)
        #pygame.display.update()
    def moveNote(self,gameDisplay,display_height,speed):
     #   pygame.draw.rect(gameDisplay, self.color, [(self.x-50),0,100,display_height])
   #     pygame.draw.rect(gameDisplay, self.dcolor, [(self.x-50),500,100,100])
        pygame.draw.circle(gameDisplay, self.lcolor, (self.x,self.y), 30, 3)
        #pygame.display.update()
        self.y = self.y + speed




    
