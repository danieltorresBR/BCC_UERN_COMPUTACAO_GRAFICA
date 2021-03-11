import OpenGL
from OpenGL.GLUT import *
from OpenGL.GL import *
from sys import argv
from random import uniform
from OpenGL.raw.GLU import gluPerspective

cotovelo = 0
mao = 0
dedos = 0
polegar = 0
indicador = 0
medio = 0
horizontal = 0

def display():
    global cotovelo, mao, dedos, polegar, indicador, medio, horizontal
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glTranslatef (0.0, 2.6, 0.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef (horizontal, 1.5, 0.0)

    ## Desenho do braco parte superior
    glPushMatrix()
    glColor3f(0.0, 0.0, 255.0) #cor do braco_superior. Funcao recebe 3 parametros (RGB) do tipo float
    glScalef (0.4, 2.0, 0.4) #glScalef(ex, ey, ez) que altera a escala do objeto ao logo dos eixos coordenados
    glutSolidCube(1.0) #glutSolidCube renderiza um cubo solido 
    glPopMatrix()

    ## Desenho do cotevelo para juncao da parte superior e inferior
    glTranslatef (0.0, -1.0, 0.0)
    glRotatef (cotovelo, 0.0, 0.0, 1.0)
    glColor3f(0.0, 0.0, 255.0)
    glutSolidSphere(0.30, 50, 50) # glutSolidSphere(GLdouble radius, GLdouble slices, GLdouble stack) renderiza uma esfera solida
    glTranslatef (0.0, -1.0, 0.0)

    ## Desenho do braco parte inferior
    glPushMatrix()
    glColor3f(0.0, 0.0, 255.0) #cor do braco_superior. Funcao recebe 3 parametros (RGB) do tipo float
    glScalef (0.4, 2.0, 0.4) #glScalef(ex, ey, ez) que altera a escala do objeto ao logo dos eixos coordenados
    glutSolidCube(1.0) #glutSolidCube renderiza um cubo solido 
    glPopMatrix()

    ## Desenho da mao
    glTranslatef (0.0, -0.6, 0.0)
    glRotatef (mao, 0.0, 1.0, 0.0)
    glTranslatef (0.0, -0.6, 0.0)
    glPushMatrix()
    glColor3f(0.0, 127.0, 255.0) #cor da mao. Funcao recebe 3 parametros (RGB) do tipo float
    glScalef (0.6, 0.3, 0.6)
    glutSolidSphere(0.70, 50, 50)  # glutSolidSphere(GLdouble radius, GLdouble slices, GLdouble stack) renderiza uma esfera solida
    glPopMatrix() # Finaliza acoes do Desenho da mao

    ## Desenho dos Dedos
    glPushMatrix()

    ## Desenho do Indicador
    glPushMatrix()
    glTranslatef (-0.2, -0.05, 0.0) #Posicao do Indicador
    glRotatef (((dedos*(-1))+indicador), 0.0, 0.0, 1.0)
    glTranslatef (-0.2, -0.3, 0.0)

    glPushMatrix() #marca o inicio
    glColor3f(255.0, 255.0, 255.0) #cor do Dedo Indicador. Funcao recebe 3 parametros (RGB) do tipo float
    glScalef (0.2, 0.6, 0.2)
    glutSolidCube (1.0)
    glPopMatrix()#marca o fim
    glPopMatrix()

    glPushMatrix()
    glTranslatef (0.2, -0.05, -0.15)
    glRotatef ((dedos+medio), 0.0, 0.0, 1.0)
    glTranslatef (0.15, -0.3, -0.15)
    glPushMatrix()
    glColor3f(0.7, 0.1, 0.3)
    glScalef (0.2, 0.6, 0.2)
    glutSolidCube (1.0)
    glPopMatrix()
    glPopMatrix()


    glPushMatrix()
    glTranslatef (0.2, -0.05, 0.15)
    glRotatef ( (dedos+polegar), 0.0, 0.0, 1.0)
    glTranslatef (0.15, -0.3, 0.15)
    glPushMatrix()
    glColor3f(0.5, 0.7, 0.4)
    glScalef (0.2, 0.6, 0.2)
    glutSolidCube (1.0)
    glPopMatrix()
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()
    glutSwapBuffers()

def modelagem (w, h):
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65.0,w / h, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef (0.0, 0.0, -5.0)

def teclas (key, x, y):
    global cotovelo, mao, dedos, polegar, indicador, medio, horizontal
    if key == 'd':
        if horizontal < 2.5:
            horizontal = horizontal + 0.1
        glutPostRedisplay()
    elif key == 'e':
        if horizontal > -2.5:
            horizontal = horizontal - 0.1
        glutPostRedisplay()
    elif key == 'r':
        if cotovelo != 110:
            cotovelo = (cotovelo + 5) % 360
        glutPostRedisplay()
    elif key == 'R':
        if cotovelo != 250:
            cotovelo = (cotovelo - 5) % 360
        glutPostRedisplay()
    elif key == 'H':
        mao = (mao + 5) % 360
        glutPostRedisplay()
    elif key == 'h':
        mao = (mao - 5) % 360
        glutPostRedisplay()
    elif key == 'T':
        if dedos != 30:
            dedos = (dedos + 5) % 360
        polegar = 0
        medio = 0
        indicador = 0
        glutPostRedisplay()
    elif key == 't':
        if dedos != 290:
            dedos = (dedos - 5) % 360
        polegar = 0
        medio = 0
        indicador = 0
        glutPostRedisplay()
    elif key == 'p':
        if polegar != 290:
            polegar = (polegar - 5) % 360
        dedos = 0
        glutPostRedisplay()
    elif key == 'P':
        if polegar != 30:
            polegar = (polegar + 5) % 360
        dedos = 0
        glutPostRedisplay()
    elif key == 'i':
        if indicador != 90:
            indicador = (indicador + 5) % 360
        dedos = 0
        glutPostRedisplay()
    elif key == 'I':
        if indicador != 330:
            indicador = (indicador - 5) % 360
        dedos = 0
        glutPostRedisplay()
    elif key == 'm':
        if medio != 295:
            medio = (medio - 5) % 360
        dedos = 0
        glutPostRedisplay()
    elif key == 'M':
        if medio != 25:
            medio = (medio + 5) % 360
        dedos = 0
        glutPostRedisplay()

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    #glutFullScreen()
    glutCreateWindow("Simulador de Braco")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(modelagem)
    glutKeyboardFunc(teclas)
    glutMainLoop()