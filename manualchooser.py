# import pygame module in this program
import pygame
import os
from pygame.locals import *
from mylib import *
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value
# for white colour
white = (255, 255, 255)

# assigning values to X and Y variable
X = 1024
Y = int(X * 16 / 9)
basedir = 'Analema/'
filelist = os.listdir(basedir)
photolist = [basedir + x for x in filelist]
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((Y, X),RESIZABLE)

# set the pygame window name
pygame.display.set_caption('Image')
count = 0
# create a surface object, image is drawn on it.
image = pygame.image.load(photolist[count])

# infinite loop
while True:

    # completely fill the surface object
    # with white colour
    display_surface.fill(white)

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(image, (0, 0))
    image = pygame.transform.scale(image, (Y, X))
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:

            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()
            events = pygame.event.get()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left',photolist[count],'deleted')
                image = pygame.image.load(photolist[count])
                image = pygame.transform.scale(image, (Y, X))
                move(photolist[count],'mandelAnalema/'+photolist[count][len(basedir):])
                display_surface.blit(image, (0, 0))
                count = count + 1
                print(count)
            elif event.key == pygame.K_RIGHT:
                print('right',photolist[count],'keeped')
                image = pygame.image.load(photolist[count])
                image = pygame.transform.scale(image, (Y, X))
                display_surface.blit(image, (0, 0))
                count = count + 1
                print(count)
            elif event.key== pygame.K_UP:
                pygame.quit()
                quit()

        # Draws the surface object to the screen.
        pygame.display.update()
