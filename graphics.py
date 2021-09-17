import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math


verticies_2D = [
    [-1, 1],
    [1, 1],
    [-1, -1]
    ]

edges_2D = [
    [0,1],
    [0,2],
    [2,1]
    ]

#Below function are hard coded to work only for triangles!

def translate(vertex, x, y):
    i = 0
    j = 0
    while i < 3:
        while j < 2:
            if j == 0:
                vertex[i][j] += x
            else:
                vertex[i][j] += y
            j += 1
        j = 0
        i += 1

def scale(vertex, x, y):
    i = 0
    j = 0
    while i < 3:
        while j < 2:
            if j == 0:
                vertex[i][j] *= x
            else:
                vertex[i][j] *= y
            j += 1
        j = 0
        i += 1

#shape shrinks as the cos and sin values get rounded down (i think)
def rotate(vertex, x):
    #glRotate(1, 0, 0, 1) # or just use the opengl native function
    i = 0
    j = 0
    while i < 3:
        while j < 2:
            if j == 0:
                vertex[i][j] = vertex[i][0] * math.cos(x) - vertex[i][1] * math.sin(x)
            else:
                vertex[i][j] = vertex[i][1] * math.cos(x) + vertex[i][0] * math.sin(x)
            j += 1
        j = 0
        i += 1

def draw():
    glBegin(GL_LINES)
    for edge in edges_2D:
        for vertex in edge:
            glVertex2fv(verticies_2D[vertex])
    glEnd()


def main():
    pygame.init()
    events = pygame.event.get()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            rotate(verticies_2D, 0.1)

        if keys[pygame.K_t]:
            rotate(verticies_2D, -0.1)

        if keys[pygame.K_s]:
            scale(verticies_2D, 1.1, 1.1)

        if keys[pygame.K_d]:
            scale(verticies_2D, 0.9, 0.9)

        if keys[pygame.K_RIGHT]:
            translate(verticies_2D, 0.1, 0)

        if keys[pygame.K_LEFT]:
            translate(verticies_2D, -0.1, 0)

        if keys[pygame.K_UP]:
            translate(verticies_2D, 0, 0.1)

        if keys[pygame.K_DOWN]:
            translate(verticies_2D, 0, -0.1)

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)


print("\nArrow Keys to move \n",
      "r and t to rotate\n",
      "s and d to scale")
main()
