import threading

import pygame
from pynput import keyboard
from pygame.locals import *
from pynput.keyboard import Key, Listener
from threading import Thread

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

flag = Key.space

def Draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def on_press(key):
    global flag
    key_press = key
    #DEBUG print("PRESSED", key_press)
    flag = key_press

def on_release(key):
    global flag
    key_press = key
    flag = Key.space


def listen():
    listener = keyboard.Listener(on_press = on_press, on_release = on_release)
    listener.start()
    listener.join()


def main():
    global flag
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glRotatef(1, 3, 9, 1)
        #if keyboard.Listener.run().__eq__(keyboard.Key.space):
        if(flag == Key.right):
            glRotatef(0.2, 0, 1, 0)
        if(flag == Key.left):
            glRotatef(0.2, 0, -1, 0)
        if(flag == Key.down):
            glRotatef(0.2, 1, 0, 0)
        if (flag == Key.up):
            glRotatef(0.2, -1, 0, 0)



        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

keyboard.Listener(on_press= on_press,on_release=on_release ).start()
threading.Thread(target =main()).start()
#thread1.join()


